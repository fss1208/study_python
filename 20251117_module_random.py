import sys, KSH
import random as rd

@KSH.func_decorator
def test_random():
    print("# random() : 임의의 실수 리턴 (0.0 <= 실수 <= 1.0)")
    print(rd.random())
    print("# randint(a,b) : 임의의 정수 리턴 (a <= 정수 <= b)")
    print(rd.randint(1, 3))                     # 1 or 2 or 3
    print(rd.randint(2, 2))                     # 2
    KSH.check_exception(rd.randint, 3, 1)       # [NG] <class 'ValueError'> empty range in randrange(3, 1)
    print("# randrange(start, stop, step=1) : 임의의 정수 리턴 (start <= 정수 < stop)")
    print(rd.randrange(1, 3))
    KSH.check_exception(rd.randrange, 3, 1)     # <class 'ValueError'> empty range in randrange(3, 1)
    print(rd.randrange(-1, 1))                  # -1 or 0
    print(rd.randrange(-3, 3, 2))               # -3 or -1 or 1
    KSH.check_exception(rd.randrange, 3, -3)    # <class 'ValueError'> empty range in randrange(3, -3)
    print("# choice(seq) : sequence에서 임의의 항목 반환 (seq = list or tuple)")
    print(rd.choice([1,2,3]))
    print(rd.choice((1,2,3)))
    #print(rd.choice({"a":1,"b":2,"c":3}))      # <class 'KeyError'>
    #print(rd.choice({1,2,3}))                  # <class 'TypeError'> 'set' object is not subscriptable
    print("# sample(papulation, k) : papulation에서 중복되지 않는 k개를 리턴 (papulation = list or tuple)")
    print(rd.sample([1,2,3,4,5], 2))            # [x, y]
    print(rd.sample([1,2,3,4,5], 1))            # [z]
    print(rd.sample([1,2,3,4,5], 0))            # []
    #print(rd.sample([1,2,3,4,5], 9))           # <class 'ValueError'> Sample larger than population or is negative
    #print(rd.sample([1,2,3,4,5], -1))          # <class 'ValueError'> Sample larger than population or is negative

#########################################################    

if (__name__ == "__main__"):
    try:
        print("# 시작")
        while (True):
            print("-" * 30)
            print("1. test_random()")
            menu = int(input("please, select menu? "))
            if (menu == 1): test_random()
            else: break
    except Exception as ex:
        print("# [NG] {} {}".format(type(ex), ex))
    else: # 예외가 발행하지 않을 때만 실행
        print("# [OK]")
    finally: # 예외 발생 여부와 관계없이 항상 실행
        print("# 종료")
