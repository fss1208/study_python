import sys, KSH
import calendar as C

@KSH.func_decorator
def test_calendar():
    print(C.calendar(2025))
    print(C.month(2025, 11))
    print(C.weekday(2025, 11, 17))      # 0 (월요일)
    print(C.weekday(2025, 11, 16))      # 6 (일요일)
    C.setfirstweekday(C.SUNDAY)
    print(C.month(2025, 11))
    print(C.isleap(2025))               # False

#########################################################    

if (__name__ == "__main__"):
    try:
        print("# 시작")
        while (True):
            print("-" * 30)
            print("1. test_calendar()")
            menu = int(input("please, select menu? "))
            if (menu == 1): test_calendar()
            else: break
    except Exception as ex:
        print("# [NG] {} {}".format(type(ex), ex))
    else: # 예외가 발행하지 않을 때만 실행
        print("# [OK]")
    finally: # 예외 발생 여부와 관계없이 항상 실행
        print("# 종료")
