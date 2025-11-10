import sys
import math

def test_io_print():
    print("# {}()".format(sys._getframe().f_code.co_name))
    print("a", "b", "c")                # a b c
    print("a", "b", "c", sep=",")       # a,b,c
    print("a", "b", "c", end="+")       # a b c+
    print()
    print("{0:>10}".format("test"))     #       test
    print("{0:^10}".format("test"))     #    test
    print("{0:<10}".format("test"))     # test      
    print("{0:4d}".format(7))           #    7
    print("{0:04d}".format(7))          # 0007
    print("{0:<4}".format(7))           # 7
    print("{0:,}".format(123456789))    # 123,456,789
    print("{0:.2f}".format(math.pi))    # 3.14
    print("{0:.2%}".format(0.12345))    # 12.35%
    print("{0:.2e}".format(9253000))    # 9.25e+06
    print("{0:#x}".format(255))         # 0xff
    print("{0:x}".format(255))          # ff
    print("{0:#o}".format(8))           # 0o10
    print("{0:o}".format(8))            # 10
    print("{0:#b}".format(2))           # 0b10
    print("{0:b}".format(2))            # 10
    name, age = "KSH", 77   
    print(f"이름:{name}, 나이:{age}")    # 이름:KSH, 나이:77 (python 3.6 버전부터 사용 가능)

def test_io_input():
    print("# {}()".format(sys._getframe().f_code.co_name))
    v = input("please, input the value? ")
    print(v)

#########################################################    

if (__name__ == "__main__"):
    try:
        print("# 시작")
        while (True):
            print("-" * 30)
            print("1. test_io_print()")
            print("2. test_io_input()")
            menu = int(input("please, select menu? "))
            if (menu == 1): test_io_print()
            elif (menu == 2): test_io_input()
            else: break
    except Exception as ex:
        print("# [NG] {} {}".format(type(ex), ex))
    else: # 예외가 발행하지 않을 때만 실행
        print("# [OK]")
    finally: # 예외 발생 여부와 관계없이 항상 실행
        print("# 종료")
