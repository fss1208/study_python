import sys

def test_tuple():
    print("# {}()".format(sys._getframe().f_code.co_name))
    tpl = (5,1,2,3,4,5)
    tpl1 = (9,) # 인자가 하나만 있는 튜플 생성                                     
    tpl2 = 10,  # 인자가 하나만 있는 튜플 생성
    print(type(tpl))
    print(tpl)
    print(tpl1)                                     # (9,)
    print(tpl2)                                     # (10,)
    print(tpl[1])                                   # 1
    print(tpl[-1])                                  # 5
    print("len = {}".format(len(tpl)))              # len = 6
    print("count(5) = {}".format(tpl.count(5)))     # count(5) = 2
    print("count(6) = {}".format(tpl.count(6)))     # count(6) = 0
    print(6 in tpl)                                 # False
    print(5 in tpl)                                 # True
    print(tpl[111])                                 # <class 'IndexError'> tuple index out of range

def test_tuple_operator():
    print("# {}()".format(sys._getframe().f_code.co_name))
    tpl1 = (1,2,3)
    tpl2 = (4,5,6)
    print(tpl1 + tpl2)      # (1, 2, 3, 4, 5, 6)
    print(tpl1 * 3)         # (1, 2, 3, 1, 2, 3, 1, 2, 3)

def test_tuple_index():
    print("# {}()".format(sys._getframe().f_code.co_name))
    tpl = (55,11,22,33,44,55)
    print(tpl)
    print(tpl.index(11))     # 1
    print(tpl.index(55))     # 0
    print(tpl.index(55))     # 0
    print(tpl.index(111))    # <class 'ValueError'> tuple.index(x): x not in tuple

def test_tuple_slicing():
    print("# {}()".format(sys._getframe().f_code.co_name))
    tpl = (0,1,2,3,4)
    print(tpl)          # (0, 1, 2, 3, 4)
    print(tpl[1:3])     # (1, 2)
    print(tpl[:3])      # (0, 1, 2)
    print(tpl[1:-1])    # (1, 2, 3)
    print(tpl[1:])      # (1, 2, 3, 4)
    print(tpl[::2])     # (0, 2, 4)
    print(tpl[::3])     # (0, 3)

def test_tuple_del():
    print("# {}()".format(sys._getframe().f_code.co_name))
    tpl = (0,1,2,3,4,5)
    print(tpl)
    del tpl[3]  # <class 'TypeError'> 'tuple' object doesn't support item deletion

#########################################################    

if (__name__ == "__main__"):
    try:
        print("# 시작")
        test_tuple()
    except Exception as ex:
        print("{} {}".format(type(ex), ex))
    else: # 예외가 발행하지 않을 때만 실행
        print("# 처리 완료")
    finally: # 예외 발생 여부와 관계없이 항상 실행
        print("# 종료")
