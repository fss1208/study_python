import sys, KSH
import numpy as np
import pandas as pd

@KSH.func_decorator
def test_pandas_series():
    s = pd.Series([11,22,33], index=["a","b","c"], name="test")
    print(type(s.values), s.values)     # <class 'pandas.core.indexes.base.Index'> Index(['a', 'b', 'c'], dtype='object')
    print(type(s.index), s.index)       # <class 'pandas.core.indexes.base.Index'> Index(['a', 'b', 'c'], dtype='object')
    print(type(s.name), s.name)         # <class 'str'> test
    print(type(s), "\n", s)
    # <class 'pandas.core.series.Series'>
    # a    11
    # b    22
    # c    33
    # Name: test, dtype: int64
    print(s["c"])       # 33
    print(s[2])         # 33 (FutureWarning)
    print(s[-1])        # 33 (FutureWarning)
    #
    s = pd.Series([11,22,33])
    print(type(s.index), s.index)       # <class 'pandas.core.indexes.range.RangeIndex'> RangeIndex(start=0, stop=3, step=1)
    print(type(s.values), s.values)     # <class 'numpy.ndarray'> [11 22 33]
    print(type(s), s)                   # <class 'pandas.core.series.Series'> 0    11 \n 1    22 \n 2    33 \n dtype:int64
    print(s[2])                         # 33
    #print(s[-1])                       # <class 'KeyError'> -1

@KSH.func_decorator
def test_pandas_series_dictionary():
    test_dict = {"a":1, "b":2, "c":3}
    s = pd.Series(test_dict)
    print(type(s), "\n", s)
    # <class 'pandas.core.series.Series'>
    # a    1
    # b    2
    # c    3
    # dtype: int64
    print("b" in s)         # True
    print("z" in s)         # False
    print(list(s.items()))  # [('a', 1), ('b', 2), ('c', 3)]
    for k, v in s.items():
        print(k, v)
    # a 1
    # b 2
    # c 3

@KSH.func_decorator
def test_pandas_series_indexing():
    s = pd.Series([11,22,33], index=["a","b","c"], name="test")
    s1 = s[["a","c"]]
    print(type(s1), "\n", s1)
    # <class 'pandas.core.series.Series'>
    # a    11
    # c    33
    # Name: test, dtype: int64
    s1["c"] = 333
    print(id(s1) == id(s))      # False
    print(s1["c"] == s["c"])    # False (깊은복사)
    print(s1["c"], s["c"])      # 333 33

@KSH.func_decorator
def test_pandas_series_selection():
    s = pd.Series([11,22,33], index=["a","b","c"], name="test")
    s3 = s[(s > 10) | (s < 30)]
    print(type(s3), "\n", s3)
    # <class 'pandas.core.series.Series'> 
    # a    11
    # b    22
    # c    33
    # Name: test, dtype: int64
    s3 = s[(s > 10) & (s < 30)]
    print(type(s3), "\n", s3)
    # <class 'pandas.core.series.Series'> 
    # a    11
    # b    22
    # Name: test, dtype: int64
    s3 = s > 30
    print(type(s3), "\n", s3)
    # <class 'pandas.core.series.Series'> 
    # a    False
    # b    False
    # c    True
    # dtype: bool
    s3 = s.index > "b"
    print(type(s.index), s.index)   # <class 'pandas.core.indexes.base.Index'> Index(['a', 'b', 'c'], dtype='object')
    print(type(s3), s3)             # <class 'numpy.ndarray'> [False False  True]

@KSH.func_decorator
def test_pandas_series_slicing():
    s = pd.Series([11,22,33], index=["a","b","c"], name="test")
    s1 = s[1:]
    print(type(s1), "\n", s1)
    # <class 'pandas.core.series.Series'>
    # b    22
    # c    33
    # Name: test, dtype: int64
    s1["c"] = 333
    print(id(s1) == id(s))      # False
    print(s1["c"] == s["c"])    # True (얕은복사)
    print(s1["c"], s["c"])      # 333 333
    s2 = s[1:2]
    print(type(s2), "\n", s2)
    # <class 'pandas.core.series.Series'>
    # b    22
    # Name: test, dtype: int64
    s2["b"] = 222
    print(id(s2) == id(s))      # False
    print(s2["b"] == s["b"])    # True (얕은복사)
    print(s2["b"], s["b"])      # 222 222

@KSH.func_decorator
def test_pandas_series_operation():
    s1 = pd.Series([1,2,3,4], index=["a","b","c","d"])
    s2 = pd.Series([2,3,4,1], index=["b","c","d","a"])
    print(type(s1), "\n", s1)
    # <class 'pandas.core.series.Series'>
    # a    1
    # b    2
    # c    3
    # d    4
    print(type(s2), "\n", s2)
    # <class 'pandas.core.series.Series'>
    # b    2
    # c    3
    # d    4
    # a    1
    s3 = s1 + s2
    print(type(s3), "\n", s3)
    # <class 'pandas.core.series.Series'>
    # a    2
    # b    4
    # c    6
    # d    8
    # dtype: int64
    s3 = s1 - s2
    print(type(s3), "\n", s3)
    # <class 'pandas.core.series.Series'>
    # a    0
    # b    0
    # c    0
    # d    0
    # dtype: int64
    s3 = s1 * s2
    print(type(s3), "\n", s3)
    # <class 'pandas.core.series.Series'>
    # a     1
    # b     4
    # c     9
    # d    16
    # dtype: int64
    s3 = s1 / s2
    print(type(s3), "\n", s3)
    # <class 'pandas.core.series.Series'>
    # a    1.0
    # b    1.0
    # c    1.0
    # d    1.0
    # dtype: float64
    s4 = pd.Series([1,2,3,4], index=["a","b","c","z"])
    s3 = s4 - s2
    print(type(s3), "\n", s3)
    # <class 'pandas.core.series.Series'>
    # a    0.0
    # b    0.0
    # c    0.0
    # d    NaN
    # z    NaN
    # dtype: float64

@KSH.func_decorator
def test_pandas_series_MAD():
    test_dict = {"a":1, "b":2, "c":3}
    s = pd.Series(test_dict)
    print(type(s), "\n", s)
    # <class 'pandas.core.series.Series'>
    # a    1
    # b    2
    # c    3
    # dtype: int64
    s["b"] = 222    # 수정
    print(type(s), "\n", s)
    # <class 'pandas.core.series.Series'>
    # a    1
    # b    222
    # c    3
    # dtype: int64
    s["d"] = 444    # 추가  
    print(type(s), "\n", s)
    # <class 'pandas.core.series.Series'>
    # a    1
    # b    222
    # c    3
    # d    444
    # dtype: int64
    del s["b"]    # 삭제
    print(type(s), "\n", s)
    # <class 'pandas.core.series.Series'>
    # a    1
    # c    3
    # d    444
    # dtype: int64

@KSH.func_decorator
def test_pandas_series_function():
    test_dict = {"a":1, "b":2, "c":3, "d":3, "e":3, "f":np.nan}
    s = pd.Series(test_dict)
    print(type(s), "\n", s)
    # <class 'pandas.core.series.Series'>
    # a    1.0
    # b    2.0
    # c    3.0
    # d    3.0
    # e    3.0
    # f    NaN
    # dtype: float64
    print(len(s), s.size)   # 6 6
    print(s.shape)          # (6,)
    print(s.unique())       # [1. 2. 3. NaN]
    print(s.nunique())      # 3 (NaN 제외)
    print(s.count())        # 5 (NaN 제외)
    print(s.sum())          # 12.0
    print(s.mean())         # 2.4
    print(s.median())       # 3.0
    print(s.std())          # 0.8944271909999159
    print(s.var())          # 0.8
    print(s.min())          # 1.0
    print(s.max())          # 3.0
    print(s.idxmin())       # a
    print(s.idxmax())       # c
    s1 = s.isnull()
    print(type(s1), "\n", s1) 
    # <class 'pandas.core.series.Series'>
    # a    False
    # b    False
    # c    False
    # d    False
    # e    False
    # f     True
    # dtype: bool
    s1 = s.isna()
    print(type(s1), "\n", s1) 
    # <class 'pandas.core.series.Series'>
    # a    False
    # b    False
    # c    False
    # d    False
    # e    False
    # f     True
    # dtype: bool
    s1 = s.notnull()
    print(type(s1), "\n", s1) 
    # <class 'pandas.core.series.Series'>
    # a     True
    # b     True
    # c     True
    # d     True
    # e     True
    # f    False
    # dtype: bool
    s1 = s.notna()
    print(type(s1), "\n", s1) 
    # <class 'pandas.core.series.Series'>
    # a     True
    # b     True
    # c     True
    # d     True
    # e     True
    # f    False
    # dtype: bool
    s1 = s.isin([1,2])
    print(type(s1), "\n", s1) 
    # <class 'pandas.core.series.Series'>
    # a    True
    # b    True
    # c    False
    # d    False
    # e    False
    # f    False
    # dtype: bool
    s1 = s.value_counts()
    print(type(s1), "\n", s1) 
    # <class 'pandas.core.series.Series'>
    # 3.0    3
    # 1.0    1
    # 2.0    1
    # Name: count, dtype: int64

@KSH.func_decorator
def test_pandas_date_range():
    print("\n# date_range(start, end, periods, freq='D') : 날짜 자동 생성")
    dt_index = pd.date_range(start='2025-11-19', end='2025-11-21')
    print(type(dt_index), dt_index)     # <class 'pandas.core.indexes.datetimes.DatetimeIndex'> DatetimeIndex(['2025-11-19', '2025-11-20', '2025-11-21'], dtype='datetime64[ns]', freq='D')
    dt_index = pd.date_range(start='2025-11-19', end='21.11.2025')
    print(type(dt_index), dt_index)     # <class 'pandas.core.indexes.datetimes.DatetimeIndex'> DatetimeIndex(['2025-11-19', '2025-11-20', '2025-11-21'], dtype='datetime64[ns]', freq='D')
    dt_index = pd.date_range(start='2025-11-19', periods=3)
    print(type(dt_index), dt_index)     # <class 'pandas.core.indexes.datetimes.DatetimeIndex'> DatetimeIndex(['2025-11-19', '2025-11-20', '2025-11-21'], dtype='datetime64[ns]', freq='D')
    dt_index = pd.date_range(start='2025-11-19', periods=3, freq="2D")
    print(dt_index) # DatetimeIndex(['2025-11-19', '2025-11-21', '2025-11-23'], dtype='datetime64[ns]', freq='2D')
    dt_index = pd.date_range(start='2025-11-19', periods=3, freq="W")
    print(dt_index) # DatetimeIndex(['2025-11-23', '2025-11-30', '2025-12-07'], dtype='datetime64[ns]', freq='W-SUN')
    dt_index = pd.date_range(start='2025-01-01', periods=6, freq="2BME")
    print(dt_index) # DatetimeIndex(['2025-01-31', '2025-03-31', '2025-05-30', '2025-07-31', '2025-09-30', '2025-11-28'], dtype='datetime64[ns]', freq='2BME')
    dt_index = pd.date_range(start='2025-01-01', periods=4, freq="QS")
    print(dt_index) # DatetimeIndex(['2025-01-01', '2025-04-01', '2025-07-01', '2025-10-01'], dtype='datetime64[ns]', freq='QS-JAN')
    dt_index = pd.date_range(start='2025-01-01 09:30', periods=3, freq="h")
    print(dt_index) # DatetimeIndex(['2025-01-01 09:30:00', '2025-01-01 10:30:00', '2025-01-01 11:30:00'], dtype='datetime64[ns]', freq='h')
    dt_index = pd.date_range(start='2025-01-01 09:30', periods=10, freq="bh")
    print(dt_index) # DatetimeIndex(['2025-01-01 09:30:00', '2025-01-01 10:30:00', '2025-01-01 11:30:00', '2025-01-01 12:30:00', '2025-01-01 13:30:00', '2025-01-01 14:30:00', '2025-01-01 15:30:00', '2025-01-01 16:30:00', '2025-01-02 09:30:00', '2025-01-02 10:30:00'], dtype='datetime64[ns]', freq='bh')
    dt_index = pd.date_range(start='2025-01-01 09:30', periods=3, freq="30min")
    print(dt_index) # DatetimeIndex(['2025-01-01 09:30:00', '2025-01-01 10:00:00', '2025-01-01 10:30:00'], dtype='datetime64[ns]', freq='30min')
    dt_index = pd.date_range(start='2025-01-01 09:30:00', periods=4, freq="45s")
    print(dt_index) # DatetimeIndex(['2025-01-01 09:30:00', '2025-01-01 09:30:45', '2025-01-01 09:31:30', '2025-01-01 09:32:15'], dtype='datetime64[ns]', freq='45s')

@KSH.func_decorator
def test_pandas_series_ex():
    print("\n# pd.Series(...) : Series 생성 (1차원 데이터 처리)")
    s = pd.Series([1,2,3])
    print(type(s.index), s.index)       # <class 'pandas.core.indexes.range.RangeIndex'> RangeIndex(start=0, stop=3, step=1)
    print(type(s.values), s.values)     # <class 'numpy.ndarray'> [1 2 3]
    print(type(s), s)                   # <class 'pandas.core.series.Series'> 0    1 \n 1    2 \n 2    3 \n dtype:int64
    s = pd.Series({"a":1, "b":2, "c":3})
    print(type(s.index), s.index)       # <class 'pandas.core.indexes.base.Index'> Index(['a', 'b', 'c'], dtype='object')
    print(type(s.values), s.values)     # <class 'numpy.ndarray'> [1 2 3]
    print(type(s), s)                   # <class 'pandas.core.series.Series'> a    1 \n b    2 \n c    3 \n dtype:int64
    s = pd.Series({"a":1.0, "b":2.0, "c":3.0})
    print(type(s.index), s.index)       # <class 'pandas.core.indexes.base.Index'> Index(['a', 'b', 'c'], dtype='object')
    print(type(s.values), s.values)     # <class 'numpy.ndarray'> [1. 2. 3.]
    print(type(s), s)                   # <class 'pandas.core.series.Series'> a    1.0 \n b    2.0 \n c    3.0 \n dtype:float64
    s = pd.Series({"a":"1", "b":"2", "c":"3"})
    print(type(s.index), s.index)       # <class 'pandas.core.indexes.base.Index'> Index(['a', 'b', 'c'], dtype='object')
    print(type(s.values), s.values)     # <class 'numpy.ndarray'> [1 2 3]
    print(type(s), s)                   # <class 'pandas.core.series.Series'> a    1 \n b    2 \n c    3 \n dtype:object
    s = pd.Series({"a":1, "b":2.0, "c":"3"})    # 문자로 변환되어 처리 (dtype:object)
    print(type(s.index), s.index)       # <class 'pandas.core.indexes.base.Index'> Index(['a', 'b', 'c'], dtype='object')
    print(type(s.values), s.values)     # <class 'numpy.ndarray'> [1 2.0 '3']
    print(type(s), s)                   # <class 'pandas.core.series.Series'> a    1 \n b    2.0 \n c    3 \n dtype:object
    s = pd.Series({"a":1, "b":2, "c":3.0})
    print(type(s.index), s.index)       # <class 'pandas.core.indexes.base.Index'> Index(['a', 'b', 'c'], dtype='object')
    print(type(s.values), s.values)     # <class 'numpy.ndarray'> [1. 2. 3.]
    print(type(s), s)                   # <class 'pandas.core.series.Series'> a    1.0 \n b    2.0 \n c    3.0 \n dtype:float64
    s = pd.Series({"a":1, "b":2, "c":np.nan})   # 실수로 변환되어 처리 (dtype:float64)
    print(type(s.index), s.index)       # <class 'pandas.core.indexes.base.Index'> Index(['a', 'b', 'c'], dtype='object')
    print(type(s.values), s.values)     # <class 'numpy.ndarray'> [1. 2. nan]
    print(type(s), s)                   # <class 'pandas.core.series.Series'> a    1.0 \n b    2.0 \n c    NaN \n dtype:float64
    s = pd.Series({"a":1, "b":np.nan, "c":"3"}) # 문자로 변환되어 처리 (dtype:object)
    print(type(s.index), s.index)       # <class 'pandas.core.indexes.base.Index'> Index(['a', 'b', 'c'], dtype='object')
    print(type(s.values), s.values)     # <class 'numpy.ndarray'> [1 NaN '3']
    print(type(s), s)                   # <class 'pandas.core.series.Series'> a    1 \n b    NaN \n c    3 \n dtype:object
    s = pd.Series([100, 200], index=["2025-11-18", "2025-11-19"])
    print(type(s.index), s.index)       # <class 'pandas.core.indexes.base.Index'> Index(['2025-11-18', '2025-11-19'], dtype='object')
    print(type(s.values), s.values)     # <class 'numpy.ndarray'> [100 200]
    print(type(s), s)                   # <class 'pandas.core.series.Series'> 2025-11-18    100 \n 2025-11-19    200 \n dtype:int64
 
if (__name__ == "__main__"):
    try:
        print("# 시작")
        while (True):
            print("-" * 30)
            print("1. test_pandas_series()")
            print("2. test_pandas_series_dictionary()")
            print("3. test_pandas_series_indexing()")
            print("4. test_pandas_series_selection()")
            print("5. test_pandas_series_slicing()")
            print("6. test_pandas_series_operation()")
            print("8. test_pandas_series_MAD()")
            print("7. test_pandas_series_function()")
            print("9. test_pandas_date_range()")
            print("10. test_pandas_series_ex()")
            menu = int(input("please, input menu number? "))
            if (menu == 1): test_pandas_series()
            elif (menu == 2): test_pandas_series_dictionary()
            elif (menu == 3): test_pandas_series_indexing()
            elif (menu == 4): test_pandas_series_selection()
            elif (menu == 5): test_pandas_series_slicing()
            elif (menu == 6): test_pandas_series_operation()
            elif (menu == 7): test_pandas_series_MAD()
            elif (menu == 8): test_pandas_series_function()
            elif (menu == 9): test_pandas_date_range()
            elif (menu == 10): test_pandas_series_ex()
            else: break
    except Exception as ex:
        print("# [NG] {} {}".format(type(ex), ex))
    else: # 예외가 발행하지 않을 때만 실행
        print("# [OK]")
    finally: # 예외 발생 여부와 관계없이 항상 실행
        print("# 종료")
