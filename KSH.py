import datetime as DT

def func_decorator(func):
    def func_info_1(*args, **dicts):
        print("-" * 30)
        print("# <{}>".format(DT.datetime.today()))
        print("# {}()".format(func.__name__))
        func(*args, **dicts)
    return func_info_1

def check_exception(func, *args):
    try:
        if (len(args) == 1):
            print(func(args[0]))
        elif (len(args) == 2):
            print(func(args[0], args[1]))
        elif (len(args) == 3):
            print(func(args[0], args[1], args[2]))
        else:
            print("Not defined!")
    except Exception as ex:
        print("# [NG] {} {}".format(type(ex), ex))
