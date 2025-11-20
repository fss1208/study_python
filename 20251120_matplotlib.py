import platform
import matplotlib as mpl
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt
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
def test_matplotlib_line():
    pass

@KSH.func_decorator
def test_matplotlib_scatter():
    pass

@KSH.func_decorator
def test_matplotlib_bar():
    pass

if (__name__ == "__main__"):
    try:
        print("# 시작")
        while (True):
            print("-" * 30)
            print("1. test_matplotlib()")
            print("2. test_matplotlib_line()")
            print("3. test_matplotlib_scatter()")
            print("4. test_matplotlib_bar()")
            menu = int(input("please, input menu number? "))
            if (menu == 1): test_matplotlib()
            elif (menu == 2): test_matplotlib_line()
            elif (menu == 3): test_matplotlib_scatter()
            elif (menu == 4): test_matplotlib_bar()
            else: break
    except Exception as ex:
        print("# [NG] {} {}".format(type(ex), ex))
    else: # 예외가 발행하지 않을 때만 실행
        print("# [OK]")
    finally: # 예외 발생 여부와 관계없이 항상 실행
        print("# 종료")
