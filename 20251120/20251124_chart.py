from matplotlib import font_manager, rc
import matplotlib as mpl
import platform

import matplotlib.pyplot as plt
import pandas as pd

class ChartManager:
    #
    def __init__(self):
        file_list = __file__.split("\\")
        load_file = __file__.replace(file_list[-1], "notExercise.csv")
        self.data_df = pd.read_csv(load_file)
        ChartManager.use_korean()

    def show_pie_chart_by_sex(self):
        plt.figure(figsize=(10,10))
        df = self.data_df[self.data_df["대분류"] == "성별"]
        index_series = df["분류"]
        self.make_pie_chart(2, 2, 1, index_series, df["운동을 할 충분한 시간이 없어서"])
        self.make_pie_chart(2, 2, 2, index_series, df["함께 운동을 할 사람이 없어서"])
        self.make_pie_chart(2, 2, 3, index_series, df["운동을 싫어해서"])
        self.make_pie_chart(2, 2, 4, index_series, df["운동을 할 만한 장소가 없어서"])
        plt.savefig("pie_chart_sex.png")
        plt.show()

    def show_pie_chart_by_age(self):
        plt.figure(figsize=(10,5))
        df = self.data_df[self.data_df["대분류"] == "연령별"]
        index_series = df["분류"]
        self.make_pie_chart(1, 3, 1, index_series, df["운동을 할 충분한 시간이 없어서"])
        self.make_pie_chart(1, 3, 2, index_series, df["함께 운동을 할 사람이 없어서"])
        self.make_pie_chart(1, 3, 3, index_series, df["운동을 할 만한 장소가 없어서"])
        plt.savefig("pie_chart_age.png")
        plt.show()

    def show_pie_chart_by_elevel(self):
        plt.figure(figsize=(18,5))
        df = self.data_df[self.data_df["대분류"] == "학력별"]
        index_series = df["분류"]
        self.make_pie_chart(1, 2, 1, index_series, df["운동을 할 충분한 시간이 없어서"])
        self.make_pie_chart(1, 2, 2, index_series, df["운동을 싫어해서"])
        plt.savefig("pie_chart_elevel.png")
        plt.show()
    
    def show_pie_chart_all(self):
        class_list = ["성별", "연령별", "학력별", "소득별", "혼인상태별", "지역대분류"]
        for class_name in class_list:
            df = self.data_df[self.data_df["대분류"] == class_name]
            index_series = df["분류"]
            plt.figure(figsize=(10,10))
            self.make_pie_chart(2, 2, 1, index_series, df["운동을 할 충분한 시간이 없어서"])
            self.make_pie_chart(2, 2, 2, index_series, df["함께 운동을 할 사람이 없어서"])
            self.make_pie_chart(2, 2, 3, index_series, df["운동을 싫어해서"])
            self.make_pie_chart(2, 2, 4, index_series, df["운동을 할 만한 장소가 없어서"])
            plt.savefig("pie_chart_{}.png".format(class_name))

    @staticmethod
    def make_pie_chart(m, n, pos, index_series, value_series):
        explode = tuple([0.01 for i in range(len(value_series))])
        plt.subplot(m, n, pos)
        plt.pie(value_series.values, labels=index_series.values, autopct="%1.1f%%", explode=explode)
        plt.title(value_series.name)

    @staticmethod
    def use_korean(): # matplotlib 기본 설정 (한글 사용시 필요)
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

if (__name__ == "__main__"):
    try:
        chart_manager = ChartManager()
        while (True):
            print("1. 성별 차트 보기")
            print("2. 연령별 차트 보기")
            print("3. 학력별 차트 보기")
            print("4. 전체 차트 보기")
            menu = int(input("메뉴를 선택해주세요 (1 ~ 4) : "))
            if (menu == 1): chart_manager.show_pie_chart_by_sex()
            elif (menu == 2): chart_manager.show_pie_chart_by_age()
            elif (menu == 3): chart_manager.show_pie_chart_by_elevel()
            elif (menu == 4): chart_manager.show_pie_chart_all()
            else: break
    except Exception as e:
        print("# [NG] {} {}".format(type(e), e))
    else: # 예외가 발행하지 않을 때만 실행
        print("# [OK]")
    finally: # 예외 발생 여부와 관계없이 항상 실행
        print("# 종료")
