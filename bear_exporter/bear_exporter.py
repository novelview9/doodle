import os
import sys
import time
import errno
import sqlite3
import datetime

# bear 시간 초기화
def set_time():
    try:
        for_days = sys.argv[1]
        for_days = int(for_days)
    except:
        for_days = 1
    local_time_set = time.localtime().tm_gmtoff
    base_time = datetime.datetime.fromtimestamp(0) - datetime.timedelta(seconds=local_time_set)
    time_gap = datetime.datetime(2001, 1, 1, 0, 0, 0) - base_time
    get_days = datetime.timedelta(days=for_days)
    node_day = datetime.datetime.now() - time_gap - get_days
    query_time_node = node_day.timestamp()
    return query_time_node, time_gap

# 가져온 데이터 딕셔너리 생성
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# 쿼리문 실행
def sqlite_io(sql_query):

    conn = sqlite3.connect(os.environ.get('BEAR_DB_PATH'))
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(sql_query)
    dataset = c.fetchall()
    return dataset



if __name__ == '__main__':

    project_root_path = os.environ.get('PROJECT_ROOT_PATH')
    output_path = os.path.join(project_root_path, 'output_md')

    try:
        os.makedirs(output_path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    query_time_node, time_gap = set_time()

    sql_query = 'SELECT ZCREATIONDATE, ZMODIFICATIONDATE, ZTITLE, ZSUBTITLE, ZTEXT FROM ZSFNOTE WHERE ZCREATIONDATE > {}'.format(query_time_node)
    dataset = sqlite_io(sql_query)
    if not dataset:
        raise "해당 기간 기록이 없습니다."


    for data in dataset:
        title = data.get('ZTITLE')
        if not title:
            title = 'Untitle'
        title = title.strip()

        _raw_create_timestemp = data.get('ZCREATIONDATE')
        _raw_modificate_timestemp = data.get('ZMODIFICATIONDATE')

        created = datetime.datetime.fromtimestamp(_raw_create_timestemp) + time_gap
        modified = datetime.datetime.fromtimestamp(_raw_modificate_timestemp) + time_gap
        text = data.get('ZTEXT')
        filename = '{}.md'.format(title).replace('/', '')
        path = os.path.join(output_path, filename)
        filename_no = 1
        while os.path.exists(path):
            filename = '{}({}).md'.format(title, filename_no).replace('/', '')
            path = os.path.join(output_path, filename)
            filename_no += 1

        print('writing..{}'.format(path))
        with open(path, 'w') as f:
            f.write(text + os.linesep)
