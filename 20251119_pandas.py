import sys, KSH
import numpy as np
import pandas as pd

@KSH.func_decorator
def test_pandas():
    pass

@KSH.func_decorator
def test_pandas_series():
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
    s = pd.Series({"a":1, "b":2.0, "c":"3"})
    print(type(s.index), s.index)       # <class 'pandas.core.indexes.base.Index'> Index(['a', 'b', 'c'], dtype='object')
    print(type(s.values), s.values)     # <class 'numpy.ndarray'> [1 2.0 '3']
    print(type(s), s)                   # <class 'pandas.core.series.Series'> a    1 \n b    2.0 \n c    3 \n dtype:object
    s = pd.Series({"a":1, "b":2.0, "c":np.nan})
    print(type(s.index), s.index)       # <class 'pandas.core.indexes.base.Index'> Index(['a', 'b', 'c'], dtype='object')
    print(type(s.values), s.values)     # <class 'numpy.ndarray'> [1.0 2.0 NaN]
    print(type(s), s)                   # <class 'pandas.core.series.Series'> a    1 \n b    2.0 \n c    3 \n dtype:float64
    s = pd.Series({"a":1, "b":np.nan, "c":"3"})
    print(type(s.index), s.index)       # <class 'pandas.core.indexes.base.Index'> Index(['a', 'b', 'c'], dtype='object')
    print(type(s.values), s.values)     # <class 'numpy.ndarray'> [1 NaN '3']
    print(type(s), s)                   # <class 'pandas.core.series.Series'> a    1 \n b    NaN \n c    3 \n dtype:object
    s = pd.Series([100, 200], index=["2025-11-18", "2025-11-19"])
    print(type(s.index), s.index)       # <class 'pandas.core.indexes.base.Index'> Index(['2025-11-18', '2025-11-19'], dtype='object')
    print(type(s.values), s.values)     # <class 'numpy.ndarray'> [100 200]
    print(type(s), s)                   # <class 'pandas.core.series.Series'> 2025-11-18    100 \n 2025-11-19    200 \n dtype:int64
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
def test_pandas_dataframe():
    print("\n# pd.DataFrame(...) : DataFrame 생성 (2차원 데이터 처리)")
    df = pd.DataFrame([[11,22,33],[44,55,66],[77,88,99]])
    print(type(df.columns), df.columns)     # <class 'pandas.core.indexes.range.RangeIndex'> RangeIndex(start=0, stop=3, step=1)
    print(type(df.index), df.index)         # <class 'pandas.core.indexes.range.RangeIndex'> RangeIndex(start=0, stop=3, step=1)
    print(type(df), "\n", df)               # <class 'pandas.core.frame.DataFrame'>
                                            #     0   1   2
                                            # 0  11  22  33
                                            # 1  44  55  66
                                            # 2  77  88  99
    table_dict = {"연도":[2023,2024,2025], "지사":["한국","미국","중국"], "고객수":[10,20,30]}
    df = pd.DataFrame(table_dict)
    print(type(df.columns), df.columns)     # <class 'pandas.core.indexes.base.Index'> Index(['연도', '지사', '고객수'], dtype='object')
    print(type(df.index), df.index)         # <class 'pandas.core.indexes.range.RangeIndex'> RangeIndex(start=0, stop=3, step=1)
    print(type(df), "\n", df)               # <class 'pandas.core.frame.DataFrame'>
                                            #    연도  지사  고객수
                                            # 0  2023  한국   10
                                            # 1  2024  미국   20
                                            # 2  2025  중국   30
    #df = pd.DataFrame({"연도":[2023,2024,2025], "지사":["한국","미국","중국"], "고객수":[10,20,30,40]}) # <class 'ValueError'> All arrays must be of the same length
    df = pd.DataFrame(table_dict, columns=["지사","고객수","연도"])
    print(type(df), "\n", df)               # <class 'pandas.core.frame.DataFrame'>
                                            #    지사  고객수  연도
                                            # 0  한국    10  2023
                                            # 1  미국    20  2024
                                            # 2  중국    30  2025

@KSH.func_decorator
def test_pandas_dataframe_statistic():
    table_data = {'봄':  [256.5, 264.3, 215.9, 223.2, 312.8],
                '여름': [770.6, 567.5, 599.8, 387.1, 446.2],
                '가을': [363.5, 231.2, 293.1, 247.7, 381.6],
                '겨울': [139.3, 59.9, 76.9, 109.1, 108.1]}
    columns_list = ['봄', '여름', '가을', '겨울']
    index_list = ['2012', '2013', '2014', '2015', '2016']
    df = pd.DataFrame(table_data, columns = columns_list, index = index_list)
    print(type(df), "\n", df)                       # <class 'pandas.core.frame.DataFrame'>
                                                    #        봄    여름    가을    겨울
                                                    # 2012  256.5  770.6  363.5  139.3
                                                    # 2013  264.3  567.5  231.2   59.9
                                                    # 2014  215.9  599.8  293.1   76.9
                                                    # 2015  223.2  387.1  247.7  109.1
                                                    # 2016  312.8  446.2  381.6  108.1
    print("\n# DataFrame.describe() 함수")
    desc = df.describe()
    print(type(desc), "\n", desc)                   # <class 'pandas.core.frame.DataFrame'>
                                                    #        봄          여름          가을          겨울
                                                    # count    5.000000    5.000000    5.000000    5.000000
                                                    # mean   254.540000  554.240000  303.420000   98.660000
                                                    # std     38.628267  148.888895   67.358496   30.925523
                                                    # min    215.900000  387.100000  231.200000   59.900000
                                                    # 25%    223.200000  446.200000  247.700000   76.900000
                                                    # 50%    256.500000  567.500000  293.100000  108.100000
                                                    # 75%    264.300000  599.800000  363.500000  109.100000
                                                    # max    312.800000  770.600000  381.600000  139.300000
    print("\n# DataFrame.mean(axis=0) 함수 :")
    dt_mean = df.mean()
    print(type(dt_mean), "\n", dt_mean)             # <class 'pandas.core.series.Series'>
                                                    # 봄     254.54
                                                    # 여름    554.24
                                                    # 가을    303.42
                                                    # 겨울     98.66
                                                    # dtype: float64
    print("\n# DataFrame.mean(axis=1) 함수 :")
    dt_mean = df.mean(axis=1)
    print(type(dt_mean), "\n", dt_mean)             # <class 'pandas.core.series.Series'>
                                                    # 2012    382.475
                                                    # 2013    280.725
                                                    # 2014    296.425
                                                    # 2015    241.775
                                                    # 2016    312.175
                                                    # dtype: float64
    print("\n# DataFrame.sum() 함수 :")
    dt_sum = df.sum()
    print(type(dt_sum), "\n", dt_sum)              # <class 'pandas.core.series.Series'>
                                                    # 봄     1272.7
                                                    # 여름    2771.2
                                                    # 가을    1517.1
                                                    # 겨울     493.6
                                                    # dtype: float64
    print("\n# DataFrame.sum(axis=1) 함수 :")
    dt_sum = df.sum(axis=1)
    print(type(dt_sum), "\n", dt_sum)               # <class 'pandas.core.series.Series'>
                                                    # 2012    1289.4
                                                    # 2013    1041.4
                                                    # 2014    1105.4
                                                    # 2015    1006.6
                                                    # 2016    1036.9
                                                    # dtype: float64
    print("\n# DataFrame.count() 함수 :")
    dt_count = df.count()
    print(type(dt_count), "\n", dt_count)           # <class 'pandas.core.series.Series'>
                                                    # 봄     5
                                                    # 여름     5
                                                    # 가을     5
                                                    # 겨울     5
                                                    # dtype: int64
    print("\n# DataFrame.count(axis=1) 함수 :")
    dt_count = df.count(axis=1)
    print(type(dt_count), "\n", dt_count)           # <class 'pandas.core.series.Series'>
                                                    # 2012    5
                                                    # 2013    5
                                                    # 2014    5
                                                    # 2015    5
                                                    # 2016    5
                                                    # dtype: int64
    print("\n# DataFrame.max() 함수 :")
    dt_max = df.max()
    print(type(dt_max), "\n", dt_max)               # <class 'pandas.core.series.Series'>
                                                    # 봄     264.3
                                                    # 여름    770.6
                                                    # 가을    363.5
                                                    # 겨울    139.3
                                                    # dtype: float64
    print("\n# DataFrame.max(axis=1) 함수 :")
    dt_max = df.max(axis=1)
    print(type(dt_max), "\n", dt_max)               # <class 'pandas.core.series.Series'>
                                                    # 2012    770.6
                                                    # 2013    567.5
                                                    # 2014    599.8
                                                    # 2015    387.1
                                                    # 2016    446.2
                                                    # dtype: float64
    print("\n# DataFrame.min() 함수 :")
    dt_min = df.min()
    print(type(dt_min), "\n", dt_min)               # <class 'pandas.core.series.Series'>
                                                    # 봄     215.9
                                                    # 여름    387.1
                                                    # 가을    231.2
                                                    # 겨울     59.9
                                                    # dtype: float64
    print("\n# DataFrame.min(axis=1) 함수 :")
    dt_min = df.min(axis=1)
    print(type(dt_min), "\n", dt_min)               # <class 'pandas.core.series.Series'>
                                                    # 2012    215.9
                                                    # 2013    231.2
                                                    # 2014    293.1
                                                    # 2015    223.2
                                                    # 2016    312.8
                                                    # dtype: float64
    print("\n# DataFrame.std() 함수 :")
    dt_std = df.std()
    print(type(dt_std), "\n", dt_std)               # <class 'pandas.core.series.Series'>
                                                    # 봄     54.24
                                                    # 여름    114.24
                                                    # 가을    54.24
                                                    # dtype: float64
    print("\n# DataFrame.std(axis=1) 함수 :")
    dt_std = df.std(axis=1)
    print(type(dt_std), "\n", dt_std)               # <class 'pandas.core.series.Series'>
                                                    # 2012    114.24
                                                    # 2013    114.24
                                                    # 2014    114.24
                                                    # 2015    114.24
                                                    # 2016    114.24
                                                    # dtype: float64
    print("\n# DataFrame.var() 함수 :")
    dt_var = df.var()
    print(type(dt_var), "\n", dt_var)               # <class 'pandas.core.series.Series'>
                                                    # 봄     2944.96
                                                    # 여름    12944.96
                                                    # 가을    2944.96
                                                    # dtype: float64
    print("\n# DataFrame.var(axis=1) 함수 :")
    dt_var = df.var(axis=1)
    print(type(dt_var), "\n", dt_var)               # <class 'pandas.core.series.Series'>
                                                    # 2012    12944.96
                                                    # 2013    12944.96
                                                    # 2014    12944.96
                                                    # 2015    12944.96
                                                    # 2016    12944.96
                                                    # dtype: float64
    print("\n# DataFrame.median() 함수 :")
    dt_median = df.median()
    print(type(dt_median), "\n", dt_median)         # <class 'pandas.core.series.Series'>
                                                    # 봄     256.5
                                                    # 여름    567.5
                                                    # 가을    363.5
                                                    # dtype: float64
    print("\n# DataFrame.median(axis=1) 함수 :")
    dt_median = df.median(axis=1)
    print(type(dt_median), "\n", dt_median)         # <class 'pandas.core.series.Series'>
                                                    # 2012    382.475
                                                    # 2013    280.725
                                                    # 2014    296.425
                                                    # 2015    241.775
                                                    # 2016    312.175
                                                    # dtype: float64
    print("\n# DataFrame.quantile() 함수 :")
    dt_quantile = df.quantile(0.5)
    print(type(dt_quantile), "\n", dt_quantile)     # <class 'pandas.core.series.Series'>
                                                    # 봄     256.5
                                                    # 여름    567.5
                                                    # 가을    363.5
                                                    # dtype: float64
    print("\n# DataFrame.quantile(axis=1) 함수 :")
    dt_quantile = df.quantile(0.5, axis=1)
    print(type(dt_quantile), "\n", dt_quantile)     # <class 'pandas.core.series.Series'>
                                                    # 2012    382.475
                                                    # 2013    280.725
                                                    # 2014    296.425
                                                    # 2015    241.775
                                                    # 2016    312.175
                                                    # dtype: float64
    print("\n# DataFrame.head() 함수 :")
    df_head = df.head()
    print(type(df_head), "\n", df_head)             # <class 'pandas.core.frame.DataFrame'>
                                                    #           봄     여름     가을     겨울
                                                    # 2012  256.5  770.6  363.5  139.3
                                                    # 2013  264.3  567.5  231.2   59.9
                                                    # 2014  215.9  599.8  293.1   76.9
                                                    # 2015  223.2  387.1  247.7  109.1
                                                    # 2016  312.8  446.2  381.6  108.1
    df_head = df.head(3)
    print(type(df_head), "\n", df_head)             # <class 'pandas.core.frame.DataFrame'>
                                                    #           봄     여름     가을     겨울
                                                    # 2012  256.5  770.6  363.5  139.3
                                                    # 2013  264.3  567.5  231.2   59.9
                                                    # 2014  215.9  599.8  293.1   76.9
    print("\n# DataFrame.tail() 함수 :")
    df_tail = df.tail()
    print(type(df_tail), "\n", df_tail)             # <class 'pandas.core.frame.DataFrame'>
                                                    #           봄     여름     가을     겨울
                                                    # 2012  256.5  770.6  363.5  139.3
                                                    # 2013  264.3  567.5  231.2   59.9
                                                    # 2014  215.9  599.8  293.1   76.9
    df_tail = df.tail(3)
    print(type(df_tail), "\n", df_tail)             # <class 'pandas.core.frame.DataFrame'>
                                                    #           봄     여름     가을     겨울
                                                    # 2012  256.5  770.6  363.5  139.3
                                                    # 2013  264.3  567.5  231.2   59.9
                                                    # 2014  215.9  599.8  293.1   76.9

#########################################################    

if (__name__ == "__main__"):
    try:
        print("# 시작")
        while (True):
            print("-" * 30)
            print("1. test_pandas_series()")
            print("2. test_pandas_dataframe()")
            print("3. test_pandas_dataframe_statistic()")
            menu = int(input("please, input menu number? "))
            if (menu == 1): test_pandas_series()
            elif (menu == 2): test_pandas_dataframe()
            elif (menu == 3): test_pandas_dataframe_statistic()
            else: break
    except Exception as ex:
        print("# [NG] {} {}".format(type(ex), ex))
    else: # 예외가 발행하지 않을 때만 실행
        print("# [OK]")
    finally: # 예외 발생 여부와 관계없이 항상 실행
        print("# 종료")
