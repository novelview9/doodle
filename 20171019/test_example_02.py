import collections

"""
case 2: 클래스에 데코레이이터 붙여서 return_one functon 에 적용하기

# 1. 데코레이터를 거쳐서 동일한 함수 반환 확인
# 2. 인스턴 메소드를 다른 메소드로 교체
# 3. 인스턴스 메소드를 데코레이터를 불러서 교체
# 4. 메소드 이름을 받아,  해당 메소드를 인스턴스 데코레이터로 불러서 교체

"""


def instance_decorator(func):

    def function_wrapper_multiple_ten(*args, **kwargs):
        result = func(*args, **kwargs)

        return result * 20

    return function_wrapper_multiple_ten


def class_decorator_do_nothing(cls):

    return cls


def class_decorator_change_instance_method(cls):
    setattr(cls, 'return_one', lambda x: 10)
    return cls


def class_decorator_apply_instance_decorator(cls):
    func = getattr(cls, 'return_one')
    setattr(cls, 'return_one', instance_decorator(func))

    return cls


def class_decorator_apply_instance_decorator_with_method_name(name):

    def decorator(cls):
        func = getattr(cls, name)
        setattr(cls, name, instance_decorator(func))

        return cls

    return decorator


class FirstStep(object):

    def return_one(self):
        return 1


@class_decorator_do_nothing
class SecondStep(object):

    def return_one(self):
        return 1


@class_decorator_change_instance_method
class ThirdStep(object):

    def return_one(self):
        return 1


@class_decorator_apply_instance_decorator
class FourthStep(object):

    def return_one(self):
        return 1


@class_decorator_apply_instance_decorator_with_method_name('return_one')
class FifthStep(object):

    def return_one(self):
        return 1

    def return_two(self):
        return 2


def test_class():
    first_step = FirstStep()
    second_step = SecondStep()
    third_step = ThirdStep()
    fourth_step = FourthStep()
    fifth_step = FifthStep()

    assert first_step.return_one() == second_step.return_one()
    assert third_step.return_one() == 10
    assert fourth_step.return_one() == 20
    assert (fifth_step.return_one() == 20) & (fifth_step.return_two() == 2)
