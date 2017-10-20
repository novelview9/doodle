# -*- coding: utf-8 -*-
import datetime
import time


"""
데코레이터 작동 순서 파악을 위해 run_order 프린트

"""

def run_order(order_no):
    print('{}번째로 수행되었습니다.'.format(order_no))


def my_logger(original_function):
    import logging
    run_order(2)
    print('format')
    logging.basicConfig(filename='{}.log'.format(original_function.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        run_order(3)
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        logging.info('[{}] 실행결과 args - {}, kwargs - {}'.format(timestamp, args, kwargs))
        return original_function(*args, **kwargs)

    return wrapper


def my_timer(original_function):
    import time
    run_order(1)
    def wrapper(*args, **kwargs):
        run_order(4)
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print('{} 함수가 실행된 총 시간: {} 초'.format(original_function.__name__, t2))
        return result

    return wrapper


@my_logger  # 1
@my_timer  # 2
def display_info(name, age):
    run_order(5)
    time.sleep(1)
    print('display_info({}, {}) 함수가 실행됐습니다.'.format(name, age))


display_info('John', 25)
