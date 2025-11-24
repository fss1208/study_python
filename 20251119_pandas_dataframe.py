import sys, KSH
import numpy as np
import pandas as pd

@KSH.func_decorator
def test_pandas_dataframe():
    print("\n# pd.DataFrame(...) : list로부터 DataFrame 생성")
    df = pd.DataFrame([[11,22,33],[44,55,66],[77,88]])
    print(type(df.columns), df.columns)     # <class 'pandas.core.indexes.range.RangeIndex'> RangeIndex(start=0, stop=3, step=1)
    print(type(df.index), df.index)         # <class 'pandas.core.indexes.range.RangeIndex'> RangeIndex(start=0, stop=3, step=1)
    print(type(df), "\n", df)
    # <class 'pandas.core.frame.DataFrame'>
    #     0   1   2
    # 0  11  22  33
    # 1  44  55  66
    # 2  77  88  NaN        
    print("\n# pd.DataFrame(...) : dict로부터 DataFrame 생성")
    table_dict = {"연도":[2023,2024,2025], "지사":["한국","미국","중국"], "고객수":[10,20,30]}
    df = pd.DataFrame(table_dict)
    print(type(df.columns), df.columns)     # <class 'pandas.core.indexes.base.Index'> Index(['연도', '지사', '고객수'], dtype='object')
    print(type(df.index), df.index)         # <class 'pandas.core.indexes.range.RangeIndex'> RangeIndex(start=0, stop=3, step=1)
    print(type(df), "\n", df)
    # <class 'pandas.core.frame.DataFrame'>
    #    연도  지사  고객수
    # 0  2023  한국   10
    # 1  2024  미국   20
    # 2  2025  중국   30
    #df = pd.DataFrame({"연도":[2023,2024,2025], "지사":["한국","미국","중국"], "고객수":[10,20,30,40]}) # <class 'ValueError'> All arrays must be of the same length
    df = pd.DataFrame(table_dict, columns=["지사","고객수","연도"])
    print(type(df), "\n", df)
    # <class 'pandas.core.frame.DataFrame'>
    #    지사  고객수  연도
    # 0  한국    10  2023
    # 1  미국    20  2024
    # 2  중국    30  2025
    print("\n# pd.DataFrame(...) : Series로부터 DataFrame 생성")
    a = pd.Series([100, 200, 300], ['a', 'b', 'd'])
    b = pd.Series([101, 201, 301], ['a', 'b', 'k'])
    c = pd.Series([110, 210, 310], ['a', 'b', 'c'])
    df = pd.DataFrame([a,b,c])
    print(type(a), "\n", a)
    # <class 'pandas.core.series.Series'>
    # a    100
    # b    200
    # d    300
    # dtype: int64
    print(type(b), "\n", b)
    # <class 'pandas.core.series.Series'>
    # a    101
    # b    201
    # k    301
    # dtype: int64
    print(type(c), "\n", c)
    # <class 'pandas.core.series.Series'>
    # a    110
    # b    210
    # c    310
    # dtype: int64
    print(type(df), "\n", df)
    # <class 'pandas.core.frame.DataFrame'>
    #        a      b      d      k      c
    # 0  100.0  200.0  300.0    NaN    NaN
    # 1  101.0  201.0    NaN  301.0    NaN
    # 2  110.0  210.0    NaN    NaN  310.0
    for column_index, column_series in df.items():
        print(type(column_index), column_index)
        for k, v in column_series.items():
            print(k, v)
        print()

@KSH.func_decorator
def test_pandas_dataframe_indexing_slicing():
    data_dict = {
        "2015": [9904312, 3448737, 2890451, 2466052],
        "2010": [9631482, 3393191, 2632035, 2000002],
        "2005": [9762546, 3512547, 2517680, 2456016],
        "2000": [9853972, 3655437, 2466338, 2473990],
        "지역": ["수도권", "경상권", "수도권", "경상권"],
        "2010-2015 증가율": [0.0283, 0.0163, 0.0982, 0.0141]
    }
    df = pd.DataFrame(data_dict)
    print(type(df), "\n", df)
    # <class 'pandas.core.frame.DataFrame'>
    #    2015  2010  2005  2000   지역  2010-2015 증가율
    # 0  9904312  9631482  9762546  9853972  수도권         0.0283
    # 1  3448737  3393191  3512547  3655437  경상권         0.0163
    # 2  2890451  2632035  2517680  2466338  수도권         0.0982
    # 3  2466052  2000002  2456016  2473990  경상권         0.0141
    print("\n# Column Indexing")
    col_series = df["2015"]
    print(type(col_series), "\n", col_series)
    # <class 'pandas.core.series.Series'>
    # 0    9904312
    # 1    3448737
    # 2    2890451
    # 3    2466052
    # Name: 2015, dtype: int64
    cell = col_series[1]
    print(type(cell), "\n", cell)
    # <class 'numpy.int64'>
    # 3448737
    print(df["2015"][1])        # 3448737
    print(df.loc[1,"2015"])     # 3448737
    print(df.iloc[1,0])         # 3448737
    #
    df1 = df[["지역"]]
    print(type(df1), "\n", df1)
    # <class 'pandas.core.frame.DataFrame'>
    #    지역
    # 0  수도권
    # 1  경상권
    # 2  수도권
    # 3  경상권
    df2 = df[["지역","2000","2010"]]
    print(type(df2), "\n", df2)
    # <class 'pandas.core.frame.DataFrame'> 
    #     지역     2000     2010
    # 0  수도권  9853972  9631482
    # 1  경상권  3655437  3393191
    # 2  수도권  2466338  2632035
    # 3  경상권  2473990  2000002
    print("\n# Row Indexing")
    df = pd.DataFrame(data_dict, index=["서울","부산","인천","대구"])
    print(type(df), "\n", df)
    # <class 'pandas.core.frame.DataFrame'>
    #        2015     2010     2005     2000   지역  2010-2015 증가율
    # 서울  9904312  9631482  9762546  9853972  수도권         0.0283
    # 부산  3448737  3393191  3512547  3655437  경상권         0.0163
    # 인천  2890451  2632035  2517680  2466338  수도권         0.0982
    # 대구  2466052  2000002  2456016  2473990  경상권         0.0141
    df1 = df[1:3]
    print(type(df1), "\n", df1)
    # <class 'pandas.core.frame.DataFrame'>
    #        2015     2010     2005     2000   지역  2010-2015 증가율
    # 부산  3448737  3393191  3512547  3655437  경상권         0.0163
    # 인천  2890451  2632035  2517680  2466338  수도권         0.0982
    df2 = df["부산":"인천"]
    print(type(df2), "\n", df2)
    # <class 'pandas.core.frame.DataFrame'>
    #        2015     2010     2005     2000   지역  2010-2015 증가율
    # 부산  3448737  3393191  3512547  3655437  경상권         0.0163
    # 인천  2890451  2632035  2517680  2466338  수도권         0.0982
    row_series = df.loc["부산"]
    print(type(row_series), "\n", row_series)
    # <class 'pandas.core.series.Series'>
    # 2015             3448737
    # 2010             3393191
    # 2005             3512547
    # 2000             3655437
    # 지역                경상권
    # 2010-2015 증가율   0.0163
    # Name: 부산, dtype: object
    row_series = df.iloc[1]
    print(type(row_series), "\n", row_series)
    # <class 'pandas.core.series.Series'>
    # 2015             3448737
    # 2010             3393191
    # 2005             3512547
    # 2000             3655437
    # 지역                경상권
    # 2010-2015 증가율   0.0163
    # Name: 부산, dtype: object
    df1 = df[:"서울"]
    print(type(df1), "\n", df1)
    # <class 'pandas.core.frame.DataFrame'>
    #        2015     2010     2005     2000   지역  2010-2015 증가율
    # 서울  9904312  9631482  9762546  9853972  수도권         0.0283
    df2 = df["서울":"인천"]
    print(type(df2), "\n", df2)
    # <class 'pandas.core.frame.DataFrame'>
    #        2015     2010     2005     2000   지역  2010-2015 증가율
    # 서울  9904312  9631482  9762546  9853972  수도권         0.0283
    # 부산  3448737  3393191  3512547  3655437  경상권         0.0163
    # 인천  2890451  2632035  2517680  2466338  수도권         0.0982
    df3 = df.iloc[1:3,1:3]
    print(type(df3), "\n", df3)
    # <class 'pandas.core.frame.DataFrame'>
    #        2010     2005
    # 부산  3393191  3512547
    # 인천  2632035  2517680
    df3 = df[["2010","2005"]]["부산":"인천"]
    print(type(df3), "\n", df3)
    # <class 'pandas.core.frame.DataFrame'>
    #        2010     2005
    # 부산  3393191  3512547
    # 인천  2632035  2517680

@KSH.func_decorator
def test_pandas_dataframe_operation():
    df1 = pd.DataFrame([[1,2,3,4,5],[6,7,8,9,10]])
    df2 = pd.DataFrame([[10,20,30],[60,70,80]])
    df3 = df1 + df2
    print(type(df3), "\n", df3)
    # <class 'pandas.core.frame.DataFrame'>
    #      0   1   2   3   4
    # 0  11  22  33 NaN NaN
    # 1  66  77  88 NaN NaN
    df4 = df1 - df2
    print(type(df4), "\n", df4)
    # <class 'pandas.core.frame.DataFrame'>
    #      0   1   2   3   4
    # 0 -9 -18 -27 NaN NaN
    # 1 -54 -63 -72 NaN NaN
    df5 = df1 * df2
    print(type(df5), "\n", df5)
    # <class 'pandas.core.frame.DataFrame'>
    #      0    1    2   3   4
    # 0   10   40   90 NaN NaN
    # 1  360  490  640 NaN NaN
    df6 = df1 / df2
    print(type(df6), "\n", df6)
    # <class 'pandas.core.frame.DataFrame'>
    #      0    1    2   3   4
    # 0  0.1  0.1  0.1 NaN NaN
    # 1  0.1  0.1  0.1 NaN NaN
    df7 = df1 % df2
    print(type(df7), "\n", df7)
    # <class 'pandas.core.frame.DataFrame'>
    #      0    1    2   3   4
    # 0    1    2    3 NaN NaN
    # 1    6    7    8 NaN NaN
    df8 = df1 ** 2
    print(type(df8), "\n", df8)
    # <class 'pandas.core.frame.DataFrame'>
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
    print(type(df), "\n", df)
    # <class 'pandas.core.frame.DataFrame'>
    #        봄    여름    가을    겨울
    # 2012  256.5  770.6  363.5  139.3
    # 2013  264.3  567.5  231.2   59.9
    # 2014  215.9  599.8  293.1   76.9
    # 2015  223.2  387.1  247.7  109.1
    # 2016  312.8  446.2  381.6  108.1
    print("\n# DataFrame.describe() 함수")
    df_desc = df.describe()
    print(type(df_desc), "\n", df_desc)
    # <class 'pandas.core.frame.DataFrame'>
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
    print(type(df_info), "\n", df_info)
    # <class 'pandas.core.frame.DataFrame'>
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
    print(type(dt_mean), "\n", dt_mean)
    # <class 'pandas.core.series.Series'>
    # 봄     254.54
    # 여름    554.24
    # 가을    303.42
    # 겨울     98.66
    # dtype: float64
    print("\n# DataFrame.mean(axis=1) 함수 :")
    dt_mean = df.mean(axis=1)
    print(type(dt_mean), "\n", dt_mean)
    # <class 'pandas.core.series.Series'>
    # 2012    382.475
    # 2013    280.725
    # 2014    296.425
    # 2015    241.775
    # 2016    312.175
    # dtype: float64
    print("\n# DataFrame.sum() 함수 :")
    dt_sum = df.sum()
    print(type(dt_sum), "\n", dt_sum)
    # <class 'pandas.core.series.Series'>
    # 봄     1272.7
    # 여름    2771.2
    # 가을    1517.1
    # 겨울     493.6
    # dtype: float64
    print("\n# DataFrame.sum(axis=1) 함수 :")
    dt_sum = df.sum(axis=1)
    print(type(dt_sum), "\n", dt_sum)
    # <class 'pandas.core.series.Series'>
    # 2012    1289.4
    # 2013    1041.4
    # 2014    1105.4
    # 2015    1006.6
    # 2016    1036.9
    # dtype: float64
    print("\n# DataFrame.count() 함수 :")
    dt_count = df.count()
    print(type(dt_count), "\n", dt_count)
    # <class 'pandas.core.series.Series'>
    # 봄     5
    # 여름     5
    # 가을     5
    # 겨울     5
    # dtype: int64
    print("\n# DataFrame.count(axis=1) 함수 :")
    dt_count = df.count(axis=1)
    print(type(dt_count), "\n", dt_count)
    # <class 'pandas.core.series.Series'>
    # 2012    5
    # 2013    5
    # 2014    5
    # 2015    5
    # 2016    5
    # dtype: int64
    print("\n# DataFrame.max() 함수 :")
    dt_max = df.max()
    print(type(dt_max), "\n", dt_max)
    # <class 'pandas.core.series.Series'>
    # 봄     264.3
    # 여름    770.6
    # 가을    363.5
    # 겨울    139.3
    # dtype: float64
    print("\n# DataFrame.max(axis=1) 함수 :")
    dt_max = df.max(axis=1)
    print(type(dt_max), "\n", dt_max)
    # <class 'pandas.core.series.Series'>
    # 2012    770.6
    # 2013    567.5
    # 2014    599.8
    # 2015    387.1
    # 2016    446.2
    # dtype: float64
    print("\n# DataFrame.min() 함수 :")
    dt_min = df.min()
    print(type(dt_min), "\n", dt_min)
    # <class 'pandas.core.series.Series'>
    # 봄     215.9
    # 여름    387.1
    # 가을    231.2
    # 겨울     59.9
    # dtype: float64
    print("\n# DataFrame.min(axis=1) 함수 :")
    dt_min = df.min(axis=1)
    print(type(dt_min), "\n", dt_min)
    # <class 'pandas.core.series.Series'>
    # 2012    215.9
    # 2013    231.2
    # 2014    293.1
    # 2015    223.2
    # 2016    312.8
    # dtype: float64
    print("\n# DataFrame.std() 함수 :")
    dt_std = df.std()
    print(type(dt_std), "\n", dt_std)
    # <class 'pandas.core.series.Series'>
    # 봄     54.24
    # 여름    114.24
    # 가을    54.24
    # dtype: float64
    print("\n# DataFrame.std(axis=1) 함수 :")
    dt_std = df.std(axis=1)
    print(type(dt_std), "\n", dt_std)
    # <class 'pandas.core.series.Series'>
    # 2012    114.24
    # 2013    114.24
    # 2014    114.24
    # 2015    114.24
    # 2016    114.24
    # dtype: float64
    print("\n# DataFrame.var() 함수 :")
    dt_var = df.var()
    print(type(dt_var), "\n", dt_var)
    # <class 'pandas.core.series.Series'>
    # 봄     2944.96
    # 여름    12944.96
    # 가을    2944.96
    # dtype: float64
    print("\n# DataFrame.var(axis=1) 함수 :")
    dt_var = df.var(axis=1)
    print(type(dt_var), "\n", dt_var)
    # <class 'pandas.core.series.Series'>
    # 2012    12944.96
    # 2013    12944.96
    # 2014    12944.96
    # 2015    12944.96
    # 2016    12944.96
    # dtype: float64
    print("\n# DataFrame.median() 함수 :")
    dt_median = df.median()
    print(type(dt_median), "\n", dt_median)
    # <class 'pandas.core.series.Series'>
    # 봄     256.5
    # 여름    567.5
    # 가을    363.5
    # dtype: float64
    print("\n# DataFrame.median(axis=1) 함수 :")
    dt_median = df.median(axis=1)
    print(type(dt_median), "\n", dt_median)
    # <class 'pandas.core.series.Series'>
    # 2012    382.475
    # 2013    280.725
    # 2014    296.425
    # 2015    241.775
    # 2016    312.175
    # dtype: float64
    print("\n# DataFrame.quantile() 함수 :")
    dt_quantile = df.quantile(0.5)
    print(type(dt_quantile), "\n", dt_quantile)
    # <class 'pandas.core.series.Series'>
    # 봄     256.5
    # 여름    567.5
    # 가을    363.5
    # dtype: float64
    print("\n# DataFrame.quantile(axis=1) 함수 :")
    dt_quantile = df.quantile(0.5, axis=1)
    print(type(dt_quantile), "\n", dt_quantile)
    # <class 'pandas.core.series.Series'>
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
    df4.loc[9] = [9, 99]
    print(type(df4), "\n", df4)
    # <class 'pandas.core.frame.DataFrame'>
    #    class1  class2
    # 0       1      11
    # 1       2      22
    # 2       3      33
    # 3       4      44
    # 4       5      55
    # 9       9      99
    df4.loc[3] = [3, 33]
    print(type(df4), "\n", df4)
    # <class 'pandas.core.frame.DataFrame'>
    #    class1  class2
    # 0       1      11
    # 1       2      22
    # 2       3      33
    # 3       3      33
    # 4       5      55
    # 9       9      99

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
    df4["class9"] = [9, 99]
    print(type(df4), "\n", df4)
    # <class 'pandas.core.frame.DataFrame'>
    #    class3  class4  class1  class2  class9
    # 0       4      44       1      11     9.0
    # 1       5      55       2      22    99.0
    df4["class1"] = [999, 999]
    print(type(df4), "\n", df4)
    # <class 'pandas.core.frame.DataFrame'>
    #    class3  class4  class1  class2  class9
    # 0       4      44     999      11       9
    # 1       5      55     999      22      99

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
def test_pandas_dataframe_drop():
    data = {
        "2015": [9904312, 3448737, 2890451, 2466052],
        "2010": [9631482, 3393191, 2632035, 2000002],
        "2005": [9762546, 3512547, 2517680, 2456016],
        "2000": [9853972, 3655437, 2466338, 2473990],
        "지역": ["수도권", "경상권", "수도권", "경상권"],
        "2010-2015 증가율": [0.0283, 0.0163, 0.0982, 0.0141]
    }
    df = pd.DataFrame(data, index=["서울","부산","인천","대구"])
    print(type(df), "\n", df)
    # <class 'pandas.core.frame.DataFrame'>
    #        2015     2010     2005     2000   지역  2010-2015 증가율
    # 서울  9904312  9631482  9762546  9853972  수도권         0.0283
    # 부산  3448737  3393191  3512547  3655437  경상권         0.0163
    # 인천  2890451  2632035  2517680  2466338  수도권         0.0982
    # 대구  2466052  2000002  2456016  2473990  경상권         0.0141       
    df1 = df.drop(index=["인천"])
    print(type(df1), "\n", df1)
    # <class 'pandas.core.frame.DataFrame'>
    #        2015     2010     2005     2000   지역  2010-2015 증가율
    # 서울  9904312  9631482  9762546  9853972  수도권         0.0283
    # 부산  3448737  3393191  3512547  3655437  경상권         0.0163
    # 대구  2466052  2000002  2456016  2473990  경상권         0.0141
    print(type(df), "\n", df)
    # <class 'pandas.core.frame.DataFrame'>
    #        2015     2010     2005     2000   지역  2010-2015 증가율
    # 서울  9904312  9631482  9762546  9853972  수도권         0.0283
    # 부산  3448737  3393191  3512547  3655437  경상권         0.0163
    # 인천  2890451  2632035  2517680  2466338  수도권         0.0982
    # 대구  2466052  2000002  2456016  2473990  경상권         0.0141
    df.drop(index=["인천"], inplace=True)
    print(type(df), "\n", df)
    # <class 'pandas.core.frame.DataFrame'>
    #        2015     2010     2005     2000   지역  2010-2015 증가율
    # 서울  9904312  9631482  9762546  9853972  수도권         0.0283
    # 부산  3448737  3393191  3512547  3655437  경상권         0.0163
    # 대구  2466052  2000002  2456016  2473990  경상권         0.0141
    df2 = df.drop(columns=["2015"])
    print(type(df2), "\n", df2)
    # <class 'pandas.core.frame.DataFrame'>
    #        2010     2005     2000   지역  2010-2015 증가율
    # 서울  9631482  9762546  9853972  수도권         0.0283
    # 부산  3393191  3512547  3655437  경상권         0.0163
    # 대구  2000002  2456016  2473990  경상권         0.0141
    print(type(df), "\n", df)
    # <class 'pandas.core.frame.DataFrame'>
    #         2015     2010     2005     2000   지역  2010-2015 증가율
    # 서울  9904312  9631482  9762546  9853972  수도권         0.0283
    # 부산  3448737  3393191  3512547  3655437  경상권         0.0163
    # 대구  2466052  2000002  2456016  2473990  경상권         0.0141
    df.drop(columns=["2015"], inplace=True)
    print(type(df), "\n", df)
    # <class 'pandas.core.frame.DataFrame'>
    #        2010     2005     2000   지역  2010-2015 증가율
    # 서울  9631482  9762546  9853972  수도권         0.0283
    # 부산  3393191  3512547  3655437  경상권         0.0163
    # 대구  2000002  2456016  2473990  경상권         0.0141
    df.drop(index=["부산"], columns=["2005"], inplace=True)
    print(type(df), "\n", df)
    # <class 'pandas.core.frame.DataFrame'>
    #        2010     2000   지역  2010-2015 증가율
    # 서울  9631482  9853972  수도권         0.0283
    # 대구  2000002  2473990  경상권         0.0141
    
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
            print("1. test_pandas_dataframe()")
            print("2. test_pandas_dataframe_indexing_slicing()")
            print("3. test_pandas_dataframe_operation()")
            print("4. test_pandas_dataframe_statistic()")
            print("5. test_pandas_dataframe_ex()")
            print("6. test_pandas_dataframe_row_concat()")
            print("7. test_pandas_dataframe_col_join()")
            print("8. test_pandas_dataframe_col_merge()")
            print("9. test_pandas_dataframe_drop()")
            print("10. test_pandas_dataframe_file()")
            menu = int(input("please, input menu number? "))
            if (menu == 1): test_pandas_dataframe()
            elif (menu == 2): test_pandas_dataframe_indexing_slicing()
            elif (menu == 3): test_pandas_dataframe_operation()
            elif (menu == 4): test_pandas_dataframe_statistic()
            elif (menu == 5): test_pandas_dataframe_ex()
            elif (menu == 6): test_pandas_dataframe_row_concat()
            elif (menu == 7): test_pandas_dataframe_col_join()
            elif (menu == 8): test_pandas_dataframe_col_merge()
            elif (menu == 9): test_pandas_dataframe_drop()
            elif (menu == 10): test_pandas_dataframe_file()
            else: break
    except Exception as ex:
        print("# [NG] {} {}".format(type(ex), ex))
    else: # 예외가 발행하지 않을 때만 실행
        print("# [OK]")
    finally: # 예외 발생 여부와 관계없이 항상 실행
        print("# 종료")
