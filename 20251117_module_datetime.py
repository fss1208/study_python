import sys, KSH
import datetime as DT

@KSH.func_decorator
def test_date():
    now = DT.date.today()
    print(type(now))                        # <class 'datetime.date'>
    print(now)                              # 2025-11-17
    print(DT.date(1234, 5, 6))              # 1234-05-06
    print(now.year, now.month, now.day)     #   
    date1 = DT.date(2025, 11, 16)
    date2 = DT.date(2025, 11, 17)
    td = date2 - date1
    print(type(td))                         # <class 'datetime.timedelta'>
    print(td)                               # 1 days, 0:00:00
    print(td.days, td.seconds)              # 1 0
    print(td.total_seconds())               # 86400.0

@KSH.func_decorator
def test_time():
    time1 = DT.time(1, 2, 3)
    time2 = DT.time(1, 3, 3)
    print(type(time1))                                                  # <class 'datetime.time'>
    print(time1)                                                        # 01:02:03
    print(time1.hour, time1.minute, time1.second, time1.microsecond)    # 1 2 3 0
    #td = time2 - time1                                                 # <class 'TypeError'> unsupported operand type(s) for -: 'datetime.time' and 'datetime.time'

@KSH.func_decorator
def test_datetime():
    now = DT.datetime.now()
    print(type(now))                                                    # <class 'datetime.datetime'>
    print(now)                                                          # 2025-11-17 16:42:17.204314
    print(now.year, now.month, now.day)                                 # 2025 11 17
    print(now.hour, now.minute, now.second, now.microsecond)            # 16 42 17 204314
    dt1 = DT.datetime.now()
    for i in range(9999999):
        pass
    dt2 = DT.datetime.now()
    td = dt2 - dt1
    print(type(td))                                                     # <class 'datetime.timedelta'>
    print(td)                                                           # 0:00:00.160904
    print(td.days, td.seconds)                                          # 0 0
    print(td.total_seconds())                                           # 0.160904

#########################################################    

if (__name__ == "__main__"):
    try:
        print("# 시작")
        while (True):
            print("-" * 30)
            print("1. test_date()")
            print("2. test_time()")
            print("3. test_datetime()")
            menu = int(input("please, select menu? "))
            if (menu == 1): test_date()
            elif (menu == 2): test_time()
            elif (menu == 3): test_datetime()
            else: break
    except Exception as ex:
        print("# [NG] {} {}".format(type(ex), ex))
    else: # 예외가 발행하지 않을 때만 실행
        print("# [OK]")
    finally: # 예외 발생 여부와 관계없이 항상 실행
        print("# 종료")
