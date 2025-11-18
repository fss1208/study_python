import sys, KSH

@KSH.func_decorator
def test_operator_is():
    a, b = 10, 10
    print("a={}({}), b={}({}) : {}, {}".format(a, id(a), b, id(b), a == b, a is b))     # a=10(140716811400392), b=10(140716811400392) : True, True
    b = 20
    print("a={}({}), b={}({}) : {}, {}".format(a, id(a), b, id(b), a == b, a is b))     # a=10(140716811400392), b=20(140716811400712) : False, False
    a = [1,2,3]
    b = [1,2,3]
    print("a={}({}), b={}({}) : {}, {}".format(a, id(a), b, id(b), a == b, a is b))     # a=[1, 2, 3](1937635321792), b=[1, 2, 3](1937635313984) : True, False
    b[1] = 22
    print("a={}({}), b={}({}) : {}, {}".format(a, id(a), b, id(b), a == b, a is b))     # a=[1, 2, 3](1937635321792), b=[1, 22, 3](1937635313984) : False, False
    a = b
    print("a={}({}), b={}({}) : {}, {}".format(a, id(a), b, id(b), a == b, a is b))     # a=[1, 22, 3](1937635313984), b=[1, 22, 3](1937635313984) : True, True
    a[1] = 2
    print("a={}({}), b={}({}) : {}, {}".format(a, id(a), b, id(b), a == b, a is b))     # a=[1, 2, 3](1937635313984), b=[1, 2, 3](1937635313984) : True, True
    b[1] = 222
    print("a={}({}), b={}({}) : {}, {}".format(a, id(a), b, id(b), a == b, a is b))     # a=[1, 222, 3](1937635313984), b=[1, 222, 3](1937635313984) : True, True

@KSH.func_decorator
def test_operator_in():
    c = [1,2,3]
    print(2 in c, 9 in c)       # True False
    c = (1,2,3)
    print(2 in c, 9 in c)       # True False
    c = {1,2,3}
    print(2 in c, 9 in c)       # True False
    c = {"a":1, "b":2, "c":3}
    print(2 in c, 9 in c)       # False False
    print("a" in c, "z" in c)   # True False

#########################################################    

if (__name__ == "__main__"):
    try:
        print("# 시작")
        while (True):
            print("-" * 30)
            print("1. test_operator_is()")
            print("2. test_operator_in()")
            menu = int(input("please, select menu? "))
            if (menu == 1): test_operator_is()
            elif (menu == 2): test_operator_in()
            else: break
    except Exception as ex:
        print("# [NG] {} {}".format(type(ex), ex))
    else: # 예외가 발행하지 않을 때만 실행
        print("# [OK]")
    finally: # 예외 발생 여부와 관계없이 항상 실행
        print("# 종료")
