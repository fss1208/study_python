import sys

def test_list():
    print("# {}()".format(sys._getframe().f_code.co_name))
    lst = [5,1,2,3,4,5]
    print(type(lst))
    print(lst)
    print(lst[1])                                   # 1
    print(lst[-1])                                  # 5
    print("len = {}".format(len(lst)))              # len = 6
    print("count(5) = {}".format(lst.count(5)))     # count(5) = 2
    print("count(6) = {}".format(lst.count(6)))     # count(6) = 0
    print(6 in lst)                                 # False
    print(5 in lst)                                 # True
    print(lst[111])                                 # <class 'IndexError'> list index out of range

def test_list_initial():
    print("# {}()".format(sys._getframe().f_code.co_name))
    lst1 = [i for i in range(10)]       # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    lst2 = [[i]*3 for i in range(3)]    # [[0, 0, 0], [1, 1, 1], [2, 2, 2]] 
    lst3 = list(range(0,10))            # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(lst1)
    print(lst2)
    print(lst3)

def test_list_operator():
    print("# {}()".format(sys._getframe().f_code.co_name))
    lst1 = [1,2,3]
    lst2 = [4,5,6]
    print(lst1 + lst2)      # [1, 2, 3, 4, 5, 6]
    print(lst1 * 3)         # [1, 2, 3, 1, 2, 3, 1, 2, 3]

def test_list_index():
    print("# {}()".format(sys._getframe().f_code.co_name))
    lst = [55,11,22,33,44,55]
    print(lst)
    print(lst.index(22))     # 2
    print(lst.index(55))     # 0
    print(lst.index(55))     # 0
    print(lst.index(111))    # <class 'ValueError'> 111 is not in list

def test_list_append():
    print("# {}()".format(sys._getframe().f_code.co_name))
    lst = [i for i in range(5)]
    print(lst)
    lst.append(10)
    print(lst)

def test_list_insert():
    print("# {}()".format(sys._getframe().f_code.co_name))
    lst = [i for i in range(5)]
    print(lst)          # [0, 1, 2, 3, 4]
    lst.insert(0, 10)
    print(lst)          # [10, 0, 1, 2, 3, 4]
    lst.insert(1, 11)
    print(lst)          # [10, 11, 0, 1, 2, 3, 4]
    lst.insert(-1, 12)
    print(lst)          # [10, 11, 0, 1, 2, 3, 12, 4]
    lst.insert(13, 13)  # 에러?
    print(lst)          # [10, 11, 0, 1, 2, 3, 12, 4, 13]

def test_list_extend():
    print("# {}()".format(sys._getframe().f_code.co_name))
    lst = [i*2 for i in range(5)]
    print(lst)              # [0, 2, 4, 6, 8]
    lst.extend([1,3,5])
    print(lst)              # [0, 2, 4, 6, 8, 1, 3, 5]

def test_list_remove():
    print("# {}()".format(sys._getframe().f_code.co_name))
    lst = [i*2+1 for i in range(5)]
    print(lst)              # [1, 3, 5, 7, 9]
    lst.extend([1,3,5])
    print(lst)              # [1, 3, 5, 7, 9, 1, 3, 5]
    lst.remove(3)
    print(lst)              # [1, 5, 7, 9, 1, 3, 5]
    lst.remove(3)
    print(lst)              # [1, 5, 7, 9, 1, 5]
    lst.remove(3)           # <class 'ValueError'> list.remove(x): x not in list
    del lst[1]
    print(lst)              # [1, 7, 9, 1, 5]

def test_list_pop():
    print("# {}()".format(sys._getframe().f_code.co_name))
    lst = [i for i in range(5)]
    print(lst)          # [0, 1, 2, 3, 4]
    print(lst.pop())    # 4
    print(lst)          # [0, 1, 2, 3]
    print(lst.pop())    # 3
    print(lst)          # [0, 1, 2]
    print(lst.pop())    # 2
    print(lst)          # [0, 1]
    print(lst.pop())    # 1
    print(lst)          # [0]
    print(lst.pop())    # 0
    print(lst)          # []
    print(lst.pop())    # <class 'IndexError'> pop from empty list

def test_list_sort_reverse():
    print("# {}()".format(sys._getframe().f_code.co_name))
    lst = [i for i in range(5)]
    print(lst)          # [0, 1, 2, 3, 4]
    lst.insert(1, 11)
    print(lst)          # [0, 11, 1, 2, 3, 4]
    lst.insert(3, 12)
    print(lst)          # [0, 11, 1, 12, 2, 3, 4]
    lst.append(10)
    print(lst)          # [0, 11, 1, 12, 2, 3, 4, 10]
    lst.reverse()
    print(lst)          # [10, 4, 3, 2, 12, 1, 11, 0]
    lst.sort()
    print(lst)          # [0, 1, 2, 3, 4, 10, 11, 12]

def test_list_slicing():
    print("# {}()".format(sys._getframe().f_code.co_name))
    lst = [i for i in range(5)]
    print(lst)          # [0, 1, 2, 3, 4]
    print(lst[1:3])     # [1, 2]
    print(lst[:3])      # [0, 1, 2]
    print(lst[1:-1])    # [1, 2, 3]
    print(lst[1:])      # [1, 2, 3, 4]
    print(lst[::2])     # [0, 2, 4]
    print(lst[::3])     # [0, 3]

#########################################################    

if (__name__ == "__main__"):
    try:
        print("# 시작")
        test_list_initial()
    except Exception as ex:
        print("{} {}".format(type(ex), ex))
    else: # 예외가 발행하지 않을 때만 실행
        print("# 처리 완료")
    finally: # 예외 발생 여부와 관계없이 항상 실행
        print("# 종료")
