import platform
import matplotlib as mpl
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys, KSH

@KSH.func_decorator
def test_matplotlib(): # matplotlib 기본 설정 (한글 사용시 필요)
    system = platform.system()
    if system == "Windows":
        font_path = "C:/Windows/Fonts/malgun.ttf"
    elif system == "Darwin":
        font_path = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
    elif system == "Linux":
        font_path = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"
    else:
        font_path = None
    if font_path:
        font = font_manager.FontProperties(fname=font_path).get_name()
        mpl.rcParams['font.family'] = font
    else:
        print("폰트 경로를 확인해주세요.")
    mpl.rcParams['axes.unicode_minus'] = False

@KSH.func_decorator
def test_matplotlib_line(): # 추세
    x = np.arange(-4.5, 5, 0.5)
    y1 = 2 * x**2
    y2 = 5 * x + 30
    y3 = 4 * x**2 + 10
    print(type(x), "\n", x )
    print(type(y1), "\n", y1)
    print(type(y2), "\n", y2)
    print(type(y3), "\n", y3)
    plt.figure(1)
    plt.plot(x, y1, ">--r", x, y2, "s-g", x, y3, "d:b")
    plt.legend(["data1", "data2", "data3"], loc=9)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Title")
    plt.grid(True)
    plt.figure(2)
    plt.plot([10, 14, 19, 20, 25])
    plt.figure(2)
    plt.clf()     # 기존 내용을 삭제
    plt.plot(x, y3)
    plt.show()

@KSH.func_decorator
def test_matplotlib_scatter():  # 관계
    city = ['seoul', 'inchun', 'daejun', 'daegu', 'woolsan', 'busan', 'kwangju']
    # 위도(latitude)와 경도(longitude)
    lat  = [37.56, 37.45, 36.35, 35.87, 35.53, 35.18, 35.16]
    lon  = [126.97, 126.70, 127.38, 128.60, 129.31, 129.07, 126.85]
    # 인구 밀도(명/km^2): 2017년 통계청 자료
    pop_den = [16154, 2751, 2839, 2790, 1099, 4454, 2995]
    size = np.array(pop_den) * 0.2 # 마커의 크기 지정
    colors = ['r', 'g', 'b', 'c', 'm', 'k', 'y'] # 마커의 컬러 지정
    plt.scatter(lon, lat, s=size, c=colors, alpha=0.5)
    plt.xlabel('longitude') # 경도
    plt.ylabel('latitude')  # 위도
    plt.show()

@KSH.func_decorator
def test_matplotlib_bar(): # 비교
    member_IDs = ['m_01', 'm_02', 'm_03', 'm_04'] # 회원 ID
    before_ex = [27, 35, 40, 33] # 운동 시작 전
    after_ex = [30, 38, 42, 37] # 운동 한 달 후
    colors = ["r", "g", "b", "m"]
    bar_width = 0.3
    data_len = len(member_IDs)
    index = np.arange(data_len)
    plt.bar(index, before_ex, tick_label=member_IDs, color=colors, width=0.9)
    plt.figure()
    plt.barh(index, before_ex, tick_label=member_IDs, color=colors) # width 사용 불가
    plt.figure()
    plt.bar(index, before_ex, color="c", align="edge", width=bar_width, label="before")
    plt.bar(index + bar_width, after_ex, color="m", align="edge", width=bar_width, label="after")
    plt.xticks(index + bar_width, member_IDs)
    plt.legend()
    plt.xlabel("ID")
    plt.ylabel("count")
    plt.title("Comparison of changes in muscle endurance before and after exercise")
    plt.show()

@KSH.func_decorator
def test_matplotlib_histogram(): # 분포
    math = [76, 82, 84, 83, 90, 86, 85, 92, 72, 71, 100, 87, 81, 76, 94, 78, 81, 60, 79, 69, 74, 87, 82, 68, 79]
    plt.hist(math, bins="auto", color="g", edgecolor="k")
    plt.figure()
    plt.hist(math, bins=15, color="g", edgecolor="k")
    plt.figure()
    plt.hist(math, color="g", edgecolor="k") # bins=10
    plt.xlabel("math score")
    plt.ylabel("frequency")
    plt.title("Distribution of math scores")
    plt.grid()
    plt.show()

@KSH.func_decorator
def test_matplotlib_pie(): # 비율
    fruit = ['사과', '바나나', '딸기', '오렌지', '포도']
    result = [7, 6, 3, 2, 2]
    explode_value = (0.1, 0, 0, 0, 0)
    plt.pie(result)
    plt.figure(figsize=(5,5))
    plt.pie(result, labels=fruit, autopct="%.1f%%")
    plt.figure(figsize=(5,5))
    plt.pie(result, labels=fruit, autopct="%.1f%%", startangle=90, counterclock=False)
    plt.figure(figsize=(5,5))
    plt.pie(result, labels=fruit, autopct="%.1f%%", startangle=90, counterclock=False, explode=explode_value)
    plt.figure(figsize=(5,5))
    plt.pie(result, labels=fruit, autopct="%.1f%%", startangle=90, counterclock=False, explode=explode_value, shadow=True)
    plt.show()

@KSH.func_decorator
def test_matplotlib_save():
    fruit = ['apple', 'banana', 'strawberry', 'orange', 'grape']
    result = [7, 6, 3, 2, 2]
    explode_value = (0.1, 0, 0, 0, 0)
    plt.pie(result, labels=fruit, autopct="%.1f%%", startangle=90, counterclock=False, explode=explode_value, shadow=True)
    plt.savefig("pie_chart_072.png") # dpi=72
    plt.savefig("pie_chart_100.png", dpi=100)
    plt.savefig("pie_chart_200.png", dpi=200)
    plt.savefig("pie_chart_200.jpg", dpi=200)

@KSH.func_decorator
def test_matplotlib_pandas_line():
    test_matplotlib()
    year = [2006, 2008, 2010, 2012, 2014, 2016] # 연도
    area = [26.2, 27.8, 28.5, 31.7, 33.5, 33.2] # 1인당 주거면적
    table = {'연도':year, '주거면적':area}
    df_area = pd.DataFrame(table, columns=['연도', '주거면적'])
    df_area.plot(x='연도', y='주거면적', grid=True, title='연도별 1인당 주거면적')
    plt.show()

@KSH.func_decorator
def test_matplotlib_pandas_scatter():
    test_matplotlib()
    temperature = [25.2, 27.4, 22.9, 26.2, 29.5, 33.1, 30.4, 36.1, 34.4, 29.1]
    Ice_cream_sales = [236500, 357500, 203500, 365200, 446600, 574200, 453200, 675400, 598400, 463100]
    dict_data = {'기온':temperature, '아이스크림 판매량':Ice_cream_sales}
    df_ice_cream = pd.DataFrame(dict_data, columns=['기온', '아이스크림 판매량'])
    df_ice_cream.plot.scatter(x='기온', y='아이스크림 판매량', grid=True, title='최고')
    #df_ice_cream.plot(kind="scatter", x='기온', y='아이스크림 판매량', grid=True, title='최고')
    plt.show()

@KSH.func_decorator
def test_matplotlib_pandas_bar():
    test_matplotlib()
    grade_num = [5, 14, 12, 3]
    students = ['A', 'B', 'C', 'D']
    df_grade = pd.DataFrame(grade_num, index=students, columns = ['Student'])
    grade_bar = df_grade.plot.bar(grid = True)
    grade_bar.set_xlabel("학점")
    grade_bar.set_ylabel("학생수")
    grade_bar.set_title("학점별 학생 수 막대 그래프")
    plt.show()

@KSH.func_decorator
def test_matplotlib_pandas_histogram():
    test_matplotlib()
    math = [76,82,84,83,90,86,85,92,72,71,100,87,81,76,
    94,78,81,60,79,69,74,87,82,68,79]
    df_math = pd.DataFrame(math, columns = ['Student'])
    math_hist = df_math.plot.hist(bins=8, grid = True)
    math_hist.set_xlabel("시험 점수")
    math_hist.set_ylabel("도수(frequency)")
    math_hist.set_title("수학 시험의 히스토그램")
    plt.show()

@KSH.func_decorator
def test_matplotlib_pandas_pie():
    test_matplotlib()
    fruit = ['사과', '바나나', '딸기', '오렌지', '포도']
    result = [7, 6, 3, 2, 2]
    df_fruit = pd.Series(result, index = fruit, name = '선택한 학생수')
    explode_value = (0.1, 0, 0, 0, 0)
    fruit_pie = df_fruit.plot.pie(figsize=(5, 5), autopct='%.1f%%', startangle=90,
    counterclock = False, explode=explode_value, shadow=True, table=True)
    fruit_pie.set_ylabel("") # 불필요한 y축 라벨 제거
    fruit_pie.set_title("과일 선호도 조사 결과")
    plt.show()

if (__name__ == "__main__"):
    try:
        print("# 시작")
        while (True):
            print("-" * 30)
            print("1. test_matplotlib()")
            print("2. test_matplotlib_line()")
            print("3. test_matplotlib_scatter()")
            print("4. test_matplotlib_bar()")
            print("5. test_matplotlib_histogram()")
            print("6. test_matplotlib_pie()")
            print("7. test_matplotlib_save()")
            print("11. test_matplotlib_pandas_line()")
            print("12. test_matplotlib_pandas_scatter()")
            print("13. test_matplotlib_pandas_bar()")
            print("14. test_matplotlib_pandas_histogram()")
            print("15. test_matplotlib_pandas_pie()")
            menu = int(input("please, input menu number? "))
            if (menu == 1): test_matplotlib()
            elif (menu == 2): test_matplotlib_line()
            elif (menu == 3): test_matplotlib_scatter()
            elif (menu == 4): test_matplotlib_bar()
            elif (menu == 5): test_matplotlib_histogram()
            elif (menu == 6): test_matplotlib_pie()
            elif (menu == 7): test_matplotlib_save()
            elif (menu == 11): test_matplotlib_pandas_line()
            elif (menu == 12): test_matplotlib_pandas_scatter()
            elif (menu == 13): test_matplotlib_pandas_bar()
            elif (menu == 14): test_matplotlib_pandas_histogram()
            elif (menu == 15): test_matplotlib_pandas_pie()
            else: break
    except Exception as ex:
        print("# [NG] {} {}".format(type(ex), ex))
    else: # 예외가 발행하지 않을 때만 실행
        print("# [OK]")
    finally: # 예외 발생 여부와 관계없이 항상 실행
        print("# 종료")
