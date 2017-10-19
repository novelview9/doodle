import collections

"""
case 1: 펑션에 데코레이터 붙이기

"""


def instance_decorator(func):

    def function_wrapper_multiple_ten(*args, **kwargs):
        result = func(*args, **kwargs)

        return result * 10

    return function_wrapper_multiple_ten


class CaseOne(object):

    @instance_decorator
    def return_one(self):
        return 1


def test_class():
    case_one = CaseOne()
    assert case_one.return_one() == 10
