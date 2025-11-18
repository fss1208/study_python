import sys, KSH
import numpy as np

def test_numpy():
    print("\n# 배열 생성")
    data = [i for i in range(6)]
    a = np.array(data)
    print(type(a), type(a.dtype), a.dtype, a)   # <class 'numpy.ndarray'> <class 'numpy.dtypes.Int64DType'> int64 [0 1 2 3 4 5]
    print("\n# 정수와 실수가 혼합된 경우 모두 실수로 변환")
    data = [0, 1, 2, 3.33, 4, 5]
    a = np.array(data)
    print(type(a), a.dtype, a)                  # <class 'numpy.ndarray'> float64 [0.   1.   2.   3.33 4.   5.  ]
    print("\n# 2차원 배열 생성")
    a = np.array([[1,2,3], [4,5,6], [7,8,9]])
    print(type(a), a.dtype, a)                  # <class 'numpy.ndarray'> int64 [[1 2 3] [4 5 6] [7 8 9]]
    #a = np.array([[1,2,3], [4,5], [7,8,9]])    # <class 'ValueError'> setting an array element with a sequence. The requested array has an inhomogeneous shape after 1 dimensions. The detected shape was (3,) + inhomogeneous part.
    print("\n# arange(start=0, stop, step=1)")
    a = np.arange(6)
    print(type(a), a.dtype, a)                  # <class 'numpy.ndarray'> int64 [0 1 2 3 4 5]
    a = np.arange(0, 6)
    print(type(a), a.dtype, a)                  # <class 'numpy.ndarray'> int64 [0 1 2 3 4 5]
    a = np.arange(0, 6, 1)
    print(type(a), a.dtype, a)                  # <class 'numpy.ndarray'> int64 [0 1 2 3 4 5]
    a = np.arange(1, 10, 2)
    print(type(a), a.dtype, a)                  # <class 'numpy.ndarray'> int64 [1 3 5 7 9]
    a = np.arange(0, 10, 2)
    print(type(a), a.dtype, a)                  # <class 'numpy.ndarray'> int64 [0 2 4 6 8]
    print("\n# reshape(...) : 배열의 차원 변환")
    a = np.arange(6).reshape(2,3)
    print(a.shape, a)                           # (2, 3) [[0 1 2] [3 4 5]]
    a = np.array([[0,1,2],[3,4,5]]).reshape(6)
    print(type(a.shape), a.shape, a)            # <class 'tuple'> (6,) [0 1 2 3 4 5]
    a = np.arange(12).reshape(3,2,2)
    print(a.shape, a)                           # (3, 2, 2) [[[ 0  1]  [ 2  3]] [[ 4  5]  [ 6  7]] [[ 8  9]  [10 11]]]
    print("\n# linspace(start, stop, num=50) : 범위의 시작과 끝을 지정하고 데이터의 개수를 지정해 배열을 생성")
    a = np.linspace(1, 10, 10)
    print(type(a), a)                           # <class 'numpy.ndarray'> [ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]
    a = np.linspace(0, 1, 10)
    print(a)                                    # [0.         0.11111111 0.22222222 0.33333333 0.44444444 0.55555556 0.66666667 0.77777778 0.88888889 1.        ]
    print("\n# zeros(...) : 모든 원소가 0인 다차원 배열 생성")
    a = np.zeros(3)
    print(type(a), a.dtype, a)                  # <class 'numpy.ndarray'> float64 [0. 0. 0.]
    a = np.zeros((2,3))
    print(a)                                    # [ [0. 0. 0.] [0. 0. 0.] ]
    a = np.zeros((2,3,2))
    print(a)                                    # [ [ [0. 0.] [0. 0.] [0. 0.] ] [ [0. 0.] [0. 0.] [0. 0.] ] ]
    print("\n# ones(...) : 모든 원소가 1인 다차원 배열 생성")
    a = np.ones(3)
    print(type(a), a.dtype, a)                  # <class 'numpy.ndarray'> float64 [1. 1. 1.]
    a = np.ones((2,3))
    print(a)                                    # [ [1. 1. 1.] [1. 1. 1.] ]
    a = np.ones((2,3,2))
    print(a)                                    # [ [ [1. 1.] [1. 1.] [1. 1.] ] [ [1. 1.] [1. 1.] [1. 1.] ] ]
    print("\n# eye(n) : n x n 단위 행렬 생성")
    a = np.eye(3)
    print(type(a), a.dtype, a)                  # <class 'numpy.ndarray'> float64 [ [1. 0. 0.] [0. 1. 0.] [0. 0. 1.] ]
    print("\n# astype(dtype) : 문자열을 숫자로 변환")
    a = np.array(["1", "2", "3"])
    print(type(a), a.dtype, a)                  # <class 'numpy.ndarray'> <U1 ['1' '2' '3']
    print(a.astype(int))                        # [1 2 3]
    print(a.astype(float))                      # [1. 2. 3.]
    a = np.array(["1.2", "3.4", "5.678"])
    print(type(a), a.dtype, a)                  # <class 'numpy.ndarray'> <U5 ['1.2' '3.4' '5.678'] : U5는 유니코드 5자리
    print(a.astype(float))                      # [1.2   3.4   5.678]
    #print(a.astype(int))                       # <class 'ValueError'> invalid literal for int() with base 10: np.str_('1.2')
    a = np.array([1,2,3.14,4,5.6])
    print(type(a), a.dtype, a)                  # <class 'numpy.ndarray'> float64 [1.   2.   3.14 4.   5.6 ]
    print(a.astype(int))                        # [1 2 3 4 5] : 실수를 정수로 변환시 버림 처리
    a = np.array([1,"2",3.14,4,5.6])
    print(type(a), a.dtype, a)                  # <class 'numpy.ndarray'> <U32 ['1' '2' '3.14' '4' '5.6']
    print(a.astype(float))                      # [1.   2.   3.14 4.   5.6 ]
    #print(a.astype(int))                       # <class 'ValueError'> invalid literal for int() with base 10: np.str_('3.14')

def test_numpy_random():
    print("\n# random.rand(...) : 0과 1사이의 난수를 갖는 실수 배열 생성")
    a = np.random.rand(3)
    print(type(a), a.dtype, a)                  # <class 'numpy.ndarray'> float64 [0.95860085 0.16179915 0.59215093]
    a = np.random.rand(3,2)
    print(type(a), a.dtype, a)                  # <class 'numpy.ndarray'> float64 [ [0.89442892 0.61271374] [0.98803061 0.16062074] [0.95201373 0.45013488] ]
    print("\n# random.rand(low, high, size) : low와 high 사이의 난수를 갖는 정수 배열 생성")
    a = np.random.randint(5)
    print(type(a), a)                           # <class 'int'> 3
    a = np.random.randint(2,5)
    print(type(a), a)                           # <class 'int'> 2
    a = np.random.randint(1,9,size=(2,3))
    print(type(a), a.dtype, a)                  # <class 'numpy.ndarray'> int32 [ [1 1 5] [1 1 2] ]

def test_numpy_operation():
    a1 = np.array([10,20,30])
    a2 = np.array([1,2,3])
    a3 = a1 + a2
    print(type(a3), a3.dtype, a3)           # <class 'numpy.ndarray'> int64 [11 22 33]
    a3 = a1 - a2
    print(type(a3), a3.dtype, a3)           # <class 'numpy.ndarray'> int64 [ 9 18 27]
    a3 = a1 * a2
    print(type(a3), a3.dtype, a3)           # <class 'numpy.ndarray'> int64 [10 40 90]
    a3 = a1 / a2
    print(type(a3), a3.dtype, a3)           # <class 'numpy.ndarray'> float64 [10. 10. 10.]
    a3 = a1 * 2
    print(type(a3), a3.dtype, a3)           # <class 'numpy.ndarray'> int64 [20 40 60]
    a3 = a2 ** 2
    print(type(a3), a3.dtype, a3)           # <class 'numpy.ndarray'> int64 [1 4 9]
    a3 = a1 > 20
    print(type(a3), a3.dtype, a3)           # <class 'numpy.ndarray'> bool [False False  True]

#########################################################    

if (__name__ == "__main__"):
    try:
        print("# 시작")
        while (True):
            print("-" * 30)
            print("1. test_numpy()")
            print("2. test_numpy_random()")
            print("3. test_numpy_operation()")
            menu = int(input("please, select menu? "))
            if (menu == 1): test_numpy()
            elif (menu == 2): test_numpy_random()
            elif (menu == 3): test_numpy_operation()
            else: break
    except Exception as ex:
        print("# [NG] {} {}".format(type(ex), ex))
    else: # 예외가 발행하지 않을 때만 실행
        print("# [OK]")
    finally: # 예외 발생 여부와 관계없이 항상 실행
        print("# 종료")
