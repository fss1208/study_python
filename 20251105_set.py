import sys

def test_set():
    print("# {}()".format(sys._getframe().f_code.co_name))
    set0 = {1,2,3,4,5}
    set1 = {1,2,3}                                     
    set2 = {1,2,3,3}                                # 중복값은 자동 제거
    set3 = {1,3,5,7,9}
    print(type(set0))
    print(set0)                                     # {1, 2, 3, 4, 5}
    print(set1)                                     # {1, 2, 3}
    print(set2)                                     # {1, 2, 3}
    print(len(set0))                                # 5
    print(len(set1))                                # 3
    print(len(set2))                                # 3
    print(set0.intersection(set3))                  # {1, 3, 5}
    print(set0 & set3)                              # {1, 3, 5}
    print(set0.union(set3))                         # {1, 2, 3, 4, 5, 7, 9}
    print(set0 | set3)                              # {1, 2, 3, 4, 5, 7, 9}
    print(set0.difference(set3))                    # {2, 4}
    print(set0 - set3)                              # {2, 4}
    print(6 in set0)                                # False
    print(5 in set0)                                # True
    print(set0[1])                                  # <class 'TypeError'> 'set' object is not subscriptable

#########################################################    

if (__name__ == "__main__"):
    try:
        print("# 시작")
        test_set()
    except Exception as ex:
        print("{} {}".format(type(ex), ex))
    else: # 예외가 발행하지 않을 때만 실행
        print("# 처리 완료")
    finally: # 예외 발생 여부와 관계없이 항상 실행
        print("# 종료")
