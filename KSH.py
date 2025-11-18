import datetime as DT

def func_decorator(func):
    def func_info_1(*args, **dicts):
        print("-" * 30)
        print("# <{}>".format(DT.datetime.today()))
        print("# {}()".format(func.__name__))
        func(*args, **dicts)
    return func_info_1

def check_exception(func, *args, **dicts):
    try:
        func(args, dicts)
    except Exception as ex:
        print("# [NG] {} {}".format(type(ex), ex))
