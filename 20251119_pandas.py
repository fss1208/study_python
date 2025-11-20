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
    print("\n# DataFrame 연산")
    df1 = pd.DataFrame([[1,2,3,4,5],[6,7,8,9,10]])
    df2 = pd.DataFrame([[10,20,30],[60,70,80]])
    df3 = df1 + df2
    print(type(df3), "\n", df3)             # <class 'pandas.core.frame.DataFrame'>
                                            #      0   1   2   3   4
                                            # 0  11  22  33 NaN NaN
                                            # 1  66  77  88 NaN NaN
    df4 = df1 - df2
    print(type(df4), "\n", df4)             # <class 'pandas.core.frame.DataFrame'>
                                            #      0   1   2   3   4
                                            # 0 -9 -18 -27 NaN NaN
                                            # 1 -54 -63 -72 NaN NaN
    df5 = df1 * df2
    print(type(df5), "\n", df5)             # <class 'pandas.core.frame.DataFrame'>
                                            #      0    1    2   3   4
                                            # 0   10   40   90 NaN NaN
                                            # 1  360  490  640 NaN NaN
    df6 = df1 / df2
    print(type(df6), "\n", df6)             # <class 'pandas.core.frame.DataFrame'>
                                            #      0    1    2   3   4
                                            # 0  0.1  0.1  0.1 NaN NaN
                                            # 1  0.1  0.1  0.1 NaN NaN
    df7 = df1 % df2
    print(type(df7), "\n", df7)             # <class 'pandas.core.frame.DataFrame'>
                                            #      0    1    2   3   4
                                            # 0    1    2    3 NaN NaN
                                            # 1    6    7    8 NaN NaN
    df8 = df1 ** 2
    print(type(df8), "\n", df8)             # <class 'pandas.core.frame.DataFrame'>
                                            #     0   1   2   3    4
                                            # 0   1   4   9  16   25
                                            # 1  36  49  64  81  100

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
                                                    #          봄          여름          가을          겨울
                                                    # count    5.000000    5.000000    5.000000    5.000000
                                                    # mean   254.540000  554.240000  303.420000   98.660000
                                                    # std     38.628267  148.888895   67.358496   30.925523
                                                    # min    215.900000  387.100000  231.200000   59.900000
                                                    # 25%    223.200000  446.200000  247.700000   76.900000
                                                    # 50%    256.500000  567.500000  293.100000  108.100000
                                                    # 75%    264.300000  599.800000  363.500000  109.100000
                                                    # max    312.800000  770.600000  381.600000  139.300000
    print("\n# DataFrame.info() 함수")
    df_info = df.info()
    print(type(df_info), "\n", df_info)             # <class 'pandas.core.frame.DataFrame'>
                                                    # Index: 5 entries, 2012 to 2016
                                                    # Data columns (total 4 columns):
                                                    #  #   Column  Non-Null Count  Dtype
                                                    # ---  ------  --------------  -----
                                                    #  0   봄       5 non-null      float64
                                                    #  1   여름      5 non-null      float64
                                                    #  2   가을      5 non-null      float64
                                                    #  3   겨울      5 non-null      float64
                                                    # dtypes: float64(4)
                                                    # memory usage: 200.0+ bytes
                                                    # <class 'NoneType'>
                                                    #  None
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

@KSH.func_decorator
def test_pandas_dataframe_ex():
    ktx_dict = {'경부선': [39060, 39896, 42005, 43621, 41702, 41266, 32427],
                '호남선': [7313, 6967, 6873, 6626, 8675, 10622, 9228],
                '경전선': [3627, 4168, 4088, 4424, 4606, 4984, 5570],
                '전라선': [309, 1771, 1954, 2244, 3146, 3945, 5766],
                '동해선': [np.nan, np.nan, np.nan, np.nan, 2395, 3786, 6667]}
    col_list = ['경부선', '호남선', '경전선', '전라선', '동해선']
    index_list = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
    df = pd.DataFrame(ktx_dict, columns = col_list, index = index_list)
    print(type(df), "\n", df)
    # <class 'pandas.core.frame.DataFrame'> 
    #       경부선    호남선   경전선   전라선     동해선
    # 2011  39060   7313  3627   309     NaN
    # 2012  39896   6967  4168  1771     NaN
    # 2013  42005   6873  4088  1954     NaN
    # 2014  43621   6626  4424  2244     NaN
    # 2015  41702   8675  4606  3146  2395.0
    # 2016  41266  10622  4984  3945  3786.0
    # 2017  32427   9228  5570  5766  6667.0
    print("\n# DataFrame.head(n=5) 함수 :")
    df_head = df.head()
    print(type(df_head), "\n", df_head)
    print(id(df) == id(df_head))
    # <class 'pandas.core.frame.DataFrame'>
    #         경부선   호남선   경전선   전라선     동해선
    # 2011  39060  7313  3627   309     NaN
    # 2012  39896  6967  4168  1771     NaN
    # 2013  42005  6873  4088  1954     NaN
    # 2014  43621  6626  4424  2244     NaN
    # 2015  41702  8675  4606  3146  2395.0
    print("\n# DataFrame.tail(n=5) 함수 :")
    df_tail = df.tail()
    print(type(df_tail), "\n", df_tail)
    print(id(df) == id(df_tail))
    # <class 'pandas.core.frame.DataFrame'>
    #         경부선    호남선   경전선   전라선     동해선
    # 2013  42005   6873  4088  1954     NaN
    # 2014  43621   6626  4424  2244     NaN
    # 2015  41702   8675  4606  3146  2395.0
    # 2016  41266  10622  4984  3945  3786.0
    # 2017  32427   9228  5570  5766  6667.0
    print("\n# DataFrame[start_index:end_index] : 행 추출하기 (end_index 미포함)")
    df_slice = df[2:5]
    print(type(df_slice), "\n", df_slice)
    # <class 'pandas.core.frame.DataFrame'>
    #       경부선  호남선 경전선 전라선   동해선
    # 2013  42005  6873  4088  1954     NaN
    # 2014  43621  6626  4424  2244     NaN
    # 2015  41702  8675  4606  3146  2395.0
    print(id(df) == id(df_slice))                           # False
    print(id(df.loc["2013"]) == id(df_slice.loc["2013"]))   # True (row 객체는 참조값으로 처리)
    print(type(df.loc["2013"]))                             # <class 'pandas.core.series.Series'>
    #
    print("\n# DataFrame.loc[start_index:end_index] : 행 추출하기 (end_index 포함)")
    df_slice = df.loc["2013":"2016"]
    print(type(df_slice), "\n", df_slice)
    # <class 'pandas.core.frame.DataFrame'>
    #       경부선  호남선 경전선  전라선  동해선
    # 2013  42005   6873  4088  1954     NaN
    # 2014  43621   6626  4424  2244     NaN
    # 2015  41702   8675  4606  3146  2395.0
    # 2016  41266  10622  4984  3945  3786.0
    print(id(df) == id(df_slice))                           # False
    print(id(df.loc["2013"]) == id(df_slice.loc["2013"]))   # True (row 객체는 참조값으로 처리)
    print(type(df.loc["2013"]))                             # <class 'pandas.core.series.Series'>
    #
    print("\n# DataFrame[column_name] : Column 가져오기")
    df_column = df["경부선"]
    print(type(df_column), "\n", df_column)
    # <class 'pandas.core.series.Series'>
    # 2011    39060
    # 2012    39896
    # 2013    42005
    # 2014    43621
    # 2015    41702
    # 2016    41266
    # 2017    32427
    # Name: 경부선, dtype: int64
    print(id(df_column) == id(df["경부선"]))                    # True
    print(id(df_column["2013"]) == id(df["경부선"]["2013"]))    # True
    #
    df_col_slice = df["경부선"]["2013":"2016"]
    print(type(df_col_slice), "\n", df_col_slice)
    # <class 'pandas.core.series.Series'>
    # 2013    42005
    # 2014    43621
    # 2015    41702
    # 2016    41266
    # Name: 경부선, dtype: int64
    print(id(df_col_slice) == id(df["경부선"]))                 # False
    print(id(df_col_slice["2013"]) == id(df["경부선"]["2013"])) # True
    #
    df_col_slice = df["경부선"][2:5]
    print(type(df_col_slice), "\n", df_col_slice)
    # <class 'pandas.core.series.Series'>
    # 2013    42005
    # 2014    43621
    # 2015    41702
    # Name: 경부선, dtype: int64
    print(id(df_col_slice) == id(df["경부선"]))                 # False
    print(id(df_col_slice["2013"]) == id(df["경부선"]["2013"])) # True
    #
    print("\n# DataFrame 중 하나의 원소 사용")
    print(df.loc["2013", "경부선"], df.iloc[2, 0])
    print(df.loc["2013"]["경부선"], df.iloc[2][0])  # FutureWarning: Series.__getitem__ treating keys as positions is deprecated. In a future version, integer keys will always be treated as labels (consistent with DataFrame behavior). To access a value by position, use `ser.iloc[pos]`.
    print(df["경부선"]["2013"], df["경부선"][2])     # FutureWarning: Series.__getitem__ treating keys as positions is deprecated. In a future version, integer keys will always be treated as labels (consistent with DataFrame behavior). To access a value by position, use `ser.iloc[pos]`.
    print(df["경부선"].loc["2013"], df["경부선"].iloc[2])
    #
    print("\n# DataFrame 행과 열을 바꾸는 방법")
    df_transpose = df.T
    print(type(df_transpose), "\n", df_transpose)
    # <class 'pandas.core.frame.DataFrame'>
    #         2011     2012     2013     2014     2015     2016     2017
    # 경부선  39060.0  39896.0  42005.0  43621.0  41702.0  41266.0  32427.0
    # 호남선   7313.0   6967.0   6873.0   6626.0   8675.0  10622.0   9228.0
    # 경전선   3627.0   4168.0   4088.0   4424.0   4606.0   4984.0   5570.0
    # 전라선    309.0   1771.0   1954.0   2244.0   3146.0   3945.0   5766.0
    # 동해선      NaN      NaN      NaN      NaN   2395.0   3786.0   6667.0
    print(id(df_transpose) == id(df)) # False
    #
    print("\n# DataFrame 열을 바꾸는 방법")
    df_col_change = df[["동해선","전라선","경전선","호남선","경부선"]]
    print(type(df_col_change), "\n", df_col_change)
    # <class 'pandas.core.frame.DataFrame'>
    #         동해선   전라선   경전선    호남선    경부선
    # 2011     NaN   309  3627   7313  39060
    # 2012     NaN  1771  4168   6967  39896
    # 2013     NaN  1954  4088   6873  42005
    # 2014     NaN  2244  4424   6626  43621
    # 2015  2395.0  3146  4606   8675  41702
    # 2016  3786.0  3945  4984  10622  41266
    # 2017  6667.0  5766  5570   9228  32427
    print(id(df_col_change) == id(df))                         # False
    print(type(df_col_change["동해선"]) == type(df["동해선"]))   # True
    #
    df_col_change = df[["동해선","전라선"]]
    print(type(df_col_change), "\n", df_col_change)
    # <class 'pandas.core.frame.DataFrame'>
    #       동해선  전라선
    # 2011    NaN   309.0
    # 2012    NaN  1771.0
    # 2013    NaN  1954.0
    # 2014    NaN  2244.0
    # 2015  2395.0  3146.0
    # 2016  3786.0  3945.0
    # 2017  6667.0  5766.0
    print(id(df_col_change) == id(df))                         # False
    print(type(df_col_change["동해선"]) == type(df["동해선"]))   # True

@KSH.func_decorator
def test_pandas_dataframe_row_concat():
    print("\n# DataFrame 행 추가하기")
    df1 = pd.DataFrame({"class1":[1,2,3],"class2":[11,22,33]})
    print(type(df1), "\n", df1)
    # <class 'pandas.core.frame.DataFrame'>
    #    class1  class2
    # 0       1      11
    # 1       2      22
    # 2       3      33
    df2 = pd.DataFrame({"class1":[4,5],"class2":[44,55]})
    print(type(df2), "\n", df2)
    # <class 'pandas.core.frame.DataFrame'>
    #    class1  class2
    # 0       4      44
    # 1       5      55
    df3 = pd.concat([df1,df2])
    print(type(df3), "\n", df3)
    # <class 'pandas.core.frame.DataFrame'>
    #    class1  class2
    # 0       1      11
    # 1       2      22
    # 2       3      33
    # 0       4      44
    # 1       5      55
    df4 = pd.concat([df1,df2], ignore_index=True)
    print(type(df4), "\n", df4)
    # <class 'pandas.core.frame.DataFrame'>
    #    class1  class2
    # 0       1      11
    # 1       2      22
    # 2       3      33
    # 3       4      44
    # 4       5      55
    #

@KSH.func_decorator
def test_pandas_dataframe_col_join():
    df1 = pd.DataFrame({"class1":[1,2,3],"class2":[11,22,33]})
    print(type(df1), "\n", df1)
    # <class 'pandas.core.frame.DataFrame'>
    #    class1  class2
    # 0       1      11
    # 1       2      22
    # 2       3      33
    df2 = pd.DataFrame({"class3":[4,5],"class4":[44,55]})
    print(type(df2), "\n", df2)
    # <class 'pandas.core.frame.DataFrame'>
    #    class3  class4
    # 0       4      44
    # 1       5      55
    print("\n# DataFrame.join() : 열 추가하기 (NaN으로 채워지는 경우)")
    df3 = df1.join(df2)
    print(type(df3), "\n", df3)
    # <class 'pandas.core.frame.DataFrame'>
    #    class1  class2  class3  class4
    # 0       1      11     4.0    44.0
    # 1       2      22     5.0    55.0
    # 2       3      33     NaN     NaN
    print("\n# DataFrame.join() 열 추가하기 (데이터 짤리는 경우)")
    df4 = df2.join(df1)
    print(type(df4), "\n", df4)
    # <class 'pandas.core.frame.DataFrame'>
    #    class3  class4  class1  class2
    # 0       4      44       1      11
    # 1       5      55       2      22

@KSH.func_decorator
def test_pandas_dataframe_col_merge():
    df1 = pd.DataFrame({"class":[0,1,2], "class1":[1,2,3],"class2":[11,22,33]})
    print(type(df1), "\n", df1)
    # <class 'pandas.core.frame.DataFrame'>
    #    class  class1  class2
    # 0      0       1      11
    # 1      1       2      22
    # 2      2       3      33
    df2 = pd.DataFrame({"class":[0,3], "class3":[4,5],"class4":[44,55]})
    print(type(df2), "\n", df2)
    # <class 'pandas.core.frame.DataFrame'>
    # class  class3  class4
    # 0      0       4      44
    # 1      3       5      55
    print("\n# DataFrame.merge(how='left') : 열 추가하기")
    df3 = df1.merge(df2, how="left", on="class")
    print(type(df3), "\n", df3)
    # <class 'pandas.core.frame.DataFrame'>
    #    class  class1  class2  class3  class4
    # 0      0       1      11     4.0    44.0
    # 1      1       2      22     NaN     NaN
    # 2      2       3      33     NaN     NaN
    print("\n# DataFrame.merge(how='right') 열 추가하기")
    df4 = df1.merge(df2, how="right", on="class")
    print(type(df4), "\n", df4)
    # <class 'pandas.core.frame.DataFrame'>
    #    class  class1  class2  class3  class4
    # 0      0     1.0    11.0       4      44
    # 1      3     NaN     NaN       5      55
    print("\n# DataFrame.merge(how='outer') 열 추가하기")
    df5 = df1.merge(df2, how="outer", on="class")
    print(type(df5), "\n", df5)
    # <class 'pandas.core.frame.DataFrame'>
    #    class  class1  class2  class3  class4
    # 0      0     1.0    11.0     4.0    44.0
    # 1      1     2.0    22.0     NaN     NaN
    # 2      2     3.0    33.0     NaN     NaN
    # 3      3     NaN     NaN     5.0    55.0
    print("\n# DataFrame.merge(how='inner') 열 추가하기")
    df6 = df1.merge(df2, how="inner", on="class")
    print(type(df6), "\n", df6)
    # <class 'pandas.core.frame.DataFrame'>
    #    class  class1  class2  class3  class4
    # 0      0     1.0    11.0     4.0    44.0

@KSH.func_decorator
def test_pandas_dataframe_file():
    py_file = __file__.split("\\")
    csv_file = __file__.replace(py_file[-1], "sea_rain1.csv")
    df = pd.read_csv(csv_file)
    print(type(df), "\n", df)
    # <class 'pandas.core.frame.DataFrame'>
    #     연도    동해     남해      서해     전체
    # 0  1996  17.4629  17.2288  14.4360  15.9067
    # 1  1997  17.4116  17.4092  14.8248  16.1526
    # 2  1998  17.5944  18.0110  15.2512  16.6044
    # 3  1999  18.1495  18.3175  14.8979  16.6284
    # 4  2000  17.9288  18.1766  15.0504  16.6178
    #
    df = pd.read_csv(csv_file, index_col="연도")
    print(type(df), "\n", df)
    # <class 'pandas.core.frame.DataFrame'> 
    #            동해       남해       서해       전체
    # 연도
    # 1996  17.4629  17.2288  14.4360  15.9067
    # 1997  17.4116  17.4092  14.8248  16.1526
    # 1998  17.5944  18.0110  15.2512  16.6044
    # 1999  18.1495  18.3175  14.8979  16.6284
    # 2000  17.9288  18.1766  15.0504  16.6178
    df.to_csv("sea_rain1_write1.csv", sep="\t", encoding="utf-8")
    #
    csv_file = __file__.replace(py_file[-1], "sea_rain1_from_notepad.csv")
    #df = pd.read_csv(csv_file)  # [NG] <class 'UnicodeDecodeError'> 'utf-8' codec can't decode byte 0xbf in position 0: invalid start byte
    df = pd.read_csv(csv_file, encoding="cp949")
    print(type(df), "\n", df)
    # <class 'pandas.core.frame.DataFrame'>
    #     연도    동해     남해      서해     전체
    # 0  1996  17.4629  17.2288  14.4360  15.9067
    # 1  1997  17.4116  17.4092  14.8248  16.1526
    # 2  1998  17.5944  18.0110  15.2512  16.6044
    # 3  1999  18.1495  18.3175  14.8979  16.6284
    # 4  2000  17.9288  18.1766  15.0504  16.6178
    df.to_csv("sea_rain1_write2.csv", sep="\t", encoding="utf-8")

if (__name__ == "__main__"):
    try:
        print("# 시작")
        while (True):
            print("-" * 30)
            print("1. test_pandas_series()")
            print("2. test_pandas_dataframe()")
            print("3. test_pandas_dataframe_statistic()")
            print("4. test_pandas_dataframe_ex()")
            print("5. test_pandas_dataframe_row_concat()")
            print("6. test_pandas_dataframe_col_join()")
            print("7. test_pandas_dataframe_col_merge()")
            print("8. test_pandas_dataframe_file()")
            menu = int(input("please, input menu number? "))
            if (menu == 1): test_pandas_series()
            elif (menu == 2): test_pandas_dataframe()
            elif (menu == 3): test_pandas_dataframe_statistic()
            elif (menu == 4): test_pandas_dataframe_ex()
            elif (menu == 5): test_pandas_dataframe_row_concat()
            elif (menu == 6): test_pandas_dataframe_col_join()
            elif (menu == 7): test_pandas_dataframe_col_merge()
            elif (menu == 8): test_pandas_dataframe_file()
            else: break
    except Exception as ex:
        print("# [NG] {} {}".format(type(ex), ex))
    else: # 예외가 발행하지 않을 때만 실행
        print("# [OK]")
    finally: # 예외 발생 여부와 관계없이 항상 실행
        print("# 종료")
