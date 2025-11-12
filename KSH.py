import datetime as DT

def func_head(func):
    def func_info_1(*args, **dicts):
        print("-" * 30)
        print("# <{}>".format(DT.datetime.today()))
        print("# {}()".format(func.__name__))
        func(*args, **dicts)
    return func_info_1

def func_tail(func):
    def func_info_2(*args, **dicts):
        print("-" * 30)
        func(*args, **dicts)
        print("# <{}>".format(DT.datetime.today()))
        print("# {}()".format(func.__name__))
    return func_info_2

def check_exception_arg1(func, arg):
    try:
        print(func(arg))
    except Exception as ex:
        print("# [NG] {} {}".format(type(ex), ex))
