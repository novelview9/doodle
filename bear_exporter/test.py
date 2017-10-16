import datetime
import sqlite3


local_time_set = time.localtime().tm_gmtoff
base_time = datetime.datetime.fromtimestamp(0) - datetime.timedelta(seconds=local_time_set)
time_gap = datetime.datetime(2001, 1, 1, 0, 0, 0) - base_time

one_day = datetime.timedelta(days=1)
two_day = datetime.timedelta(days=2)
in_week = datetime.timedelta(days=7)

bear_one_day_ago = datetime.datetime.now() - time_gap - in_week
query_time_node = bear_one_day_ago.timestamp()

sql_query = 'SELECT ZCREATIONDATE, ZMODIFICATIONDATE, ZTITLE, ZSUBTITLE, ZTEXT FROM ZSFNOTE WHERE ZCREATIONDATE >{}'.format(query_time_node)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

conn = sqlite3.connect('database.sqlite')
conn.row_factory = dict_factory
c = conn.cursor()

c.execute(sql_query)
dataset = c.fetchall()
for data in dataset:
    title = data.get('ZTITLE',)
    _raw_create_timestemp = data.get('ZCREATIONDATE')
    _raw_modificate_timestemp = data.get('ZMODIFICATIONDATE')
    created = datetime.datetime.fromtimestamp(_raw_create_timestemp) + time_gap
    modified = datetime.datetime.fromtimestamp(_raw_modificate_timestemp) + time_gap
    text = data.get('ZTEXT')

from IPython import embed;embed()
