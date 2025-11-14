import KSH

a = 5 # 전역변수

@KSH.func_decorator
def test_function_local():
    a = 111
    print(a)

@KSH.func_decorator
def test_function_global_2():
    print(a)

@KSH.func_decorator
def test_function_global_3():
    global a    # 함수 안에서 전역변수의 내용을 변경하기 위해 반드시 선언
    a = 333
    print(a)

@KSH.func_decorator
def test_function_global_4():
    a += 1      # <class 'UnboundLocalError'> cannot access local variable 'a' where it is not associated with a value
    print(a)    # a가 지역변수로 생성되기 전에 사용되어 에러 발생 (a += 1 >> a = a + 1)

@KSH.func_decorator
def test_function_lamda():
    ld_func = lambda x : x**2
    print(ld_func(2))
    print((lambda x : x ** 2)(2))

@KSH.func_decorator
def test_function_built_in():
    print("# int 함수 : 실수나 문자열을 정수로 변환 (실수의 경우 소수점 이하는 버리는 방식)")
    print(int(0.123), int(3.912), int(-1.999), int("123"))      # 0 3 -1 123
    KSH.check_exception(int, "123d")                # <class 'ValueError'> invalid literal for int() with base 10: '123d'
    KSH.check_exception(int, "12.3")                # <class 'ValueError'> invalid literal for int() with base 10: '12.3'
    print("# float 함수 : 정수나 문자열을 실수로 변환")
    print(float(0), float(123), float(-123), float("1.23"))     # 0.0 123.0 -123.0 1.23
    KSH.check_exception(float, "0.123f")            # <class 'ValueError'> could not convert string to float: '0.123f'
    KSH.check_exception(int, "123")                 # 123
    print("# str 함수 : 정수나 실수를 문자열로 변환")
    print(str(123), str(-123), str(0.123), str(12.3), (-12.3))  # 123 -123 0.123 12.3 -12.3
    print("# 형 변환 함수")
    print(list((1,2,3)), list({1,2,3}))
    print(tuple([1,2,3]), tuple({1,2,3}))
    print(set([1,2,3]), set((1,2,3)))
    print("# 형 확인 함수 : 데이터 타입을 확인")
    print(type(123), type(1.23), type("123"))   # <class 'int'> <class 'float'> <class 'str'>
    print(type([]), type(()), type({}))         # <class 'list'> <class 'tuple'> <class 'dict'>
    print("# bool 함수 : 숫자를 True 또는 False로 변환")
    print(bool(0), bool(0.0))                                   # False False
    print(bool(123), bool(-123), bool(1.23), bool(-1.23))       # True True True True
    print(bool("adf"), bool(" "), bool(""), bool(None))         # True True False False
    print(bool([1,2,3]), bool([]))                              # True False
    print(bool((1,2,3)), bool(()))                              # True False
    print(bool({1,2,3}), bool({}))                              # True False
    print("# min & max 함수 : 최소값과 최대값을 찾음")
    print(min([1,2,3]), max([1,2,3]))                           # 1 3
    print(min((1,2,3)), max((1,2,3)))                           # 1 3
    print(min({1,2,3}), max({1,2,3}))                           # 1 3
    print(min("AaBbC"), max("AaBbC"))                           # A b
    print(min({"Abc","abc","bcd","bce"}))                       # Abc
    print(max({"Abc","abc","bcd","bce"}))                       # bce
    print("# abs 함수 : 절대값")
    print(abs(123), abs(-123))                                  # 123 123
    print(abs(1.23), abs(-1.23))                                # 1.23 1.23
    print("# sum 함수 : 전체합")
    print(sum([1,2,3]))                                         # 6
    print(sum((1,2,3)))                                         # 6
    print(sum({1,2,3}))                                         # 6
    KSH.check_exception(sum, ["1","22","333"])      # <class 'TypeError'> unsupported operand type(s) for +: 'int' and 'str'

@KSH.func_decorator
def test_function_default_arg(year, month, day = 1):
    print("{}-{}-{}".format(year, month, day))

@KSH.func_decorator
def test_function_Keyword_arg(year, month, day):
    print("{}-{}-{}".format(year, month, day))

@KSH.func_decorator
def test_function_variable_arg(*args, **dicts):
    print(type(args))
    print(type(dicts))

@KSH.func_decorator
def test_function_overap():
    a = 1
    def inner1():
        b = 2
        def inner2():
            c = 3
            print(a,b,c)
        inner2()
    inner1()

@KSH.func_decorator
def test_function_decorator():
    print("Test Decorator!")

#########################################################    

if (__name__ == "__main__"):
    try:
        print("# 시작")
        while (True):
            print("-" * 30)
            print("1. test_function_local()")
            print("2. test_function_global_2()")
            print("3. test_function_global_3()")
            print("4. test_function_global_4()")
            print("5. test_function_lamda()")
            print("6. test_function_built_in()")
            print("7. test_function_default_arg()")
            print("8. test_function_Keyword_arg()")
            print("9. test_function_variable_arg()")
            print("10. test_function_overap()")
            print("11. test_function_decorator()")
            menu = int(input("please, select menu? "))
            if (menu == 1): test_function_local()
            elif (menu == 2): test_function_global_2()
            elif (menu == 3): test_function_global_3()
            elif (menu == 4): test_function_global_4()
            elif (menu == 5): test_function_lamda()
            elif (menu == 6): test_function_built_in()
            elif (menu == 7): test_function_default_arg(2025,11)
            elif (menu == 8): test_function_Keyword_arg(day=12,month=11,year=2025)
            elif (menu == 9): test_function_variable_arg()
            elif (menu == 10): test_function_overap()
            elif (menu == 11): test_function_decorator()
            else: break
    except Exception as ex:
        print("# [NG] {} {}".format(type(ex), ex))
    else: # 예외가 발행하지 않을 때만 실행
        print("# [OK]")
    finally: # 예외 발생 여부와 관계없이 항상 실행
        print("# 종료")
