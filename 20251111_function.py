import sys

a = 5

def test_function_local():
    print("# {}()".format(sys._getframe().f_code.co_name))
    a = 111
    print(a)

def test_function_global_2():
    print("# {}()".format(sys._getframe().f_code.co_name))
    print(a)

def test_function_global_3():
    print("# {}()".format(sys._getframe().f_code.co_name))
    global a
    a = 333
    print(a)

#########################################################    

if (__name__ == "__main__"):
    try:
        print("# 시작")
        while (True):
            print("-" * 30)
            print("1. test_function_local()")
            print("2. test_function_global_2()")
            print("3. test_function_global_3()")
            menu = int(input("please, select menu? "))
            if (menu == 1): test_function_local()
            elif (menu == 2): test_function_global_2()
            elif (menu == 3): test_function_global_3()
            else: break
    except Exception as ex:
        print("# [NG] {} {}".format(type(ex), ex))
    else: # 예외가 발행하지 않을 때만 실행
        print("# [OK]")
    finally: # 예외 발생 여부와 관계없이 항상 실행
        print("# 종료")
