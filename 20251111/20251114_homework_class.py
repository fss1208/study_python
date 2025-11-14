import os

class StudentError(Exception):
    def __init__(self, msg):
        self.msg = msg

class RowData:
    #
    cell_width = 10
    #
    def __init__(self, key_list, value_list):
        if ((len(key_list) == 0) or (len(value_list) == 0) or (len(key_list) != len(value_list))):
            raise StudentError("KEY와 VALUE의 개수 불일치! (keys={},values={})".format(len(key_list), len(value_list)))
        self.__row_dict = {}
        for i in range(len(key_list)):
            self.__row_dict[key_list[i]] = value_list[i]
    #
    def print_screen(self):
        for k, v in self.__row_dict.items():
            print(RowData.to_cell_string(v) if (v is str) else RowData.to_cell_string(str(v)), end="")
        print()
    #
    def write_file(self, f):
        for k, v in self.__row_dict.items():
            f.write(RowData.to_cell_string(v) if (v is str) else RowData.to_cell_string(str(v)))
        f.write("\n")
    #
    def set_cell(self, key, value):
        if (key not in self.__row_dict):
            raise StudentError("'{}'는 존재하지 않는 KEY 입니다!".format(key))
        self.__row_dict[key] = value
    #
    def get_cell(self, key):
        if (key not in self.__row_dict):
            raise StudentError("'{}'는 존재하지 않는 KEY 입니다!".format(key))
        return self.__row_dict[key]
    #
    @staticmethod
    def to_cell_string(cell_string):
        return cell_string.center(RowData.cell_width, " ")

class StudentRowData(RowData):
    #
    sum_key = "sum"
    avg_key = "avg"
    input_key_list = ["name", "kor", "mat", "eng", "sci"]
    total_key_list = ["name", "kor", "mat", "eng", "sci", sum_key, avg_key]
    title_list = ["NAME", "KOREAN", "MATH", "ENGLISH", "SCIENCE", "SUM", "AVERAGE"]
    #
    def __init__(self, input_string_list):
        if (len(input_string_list) == len(StudentRowData.input_key_list)):
            input_string_list.append("0")   # sum
            input_string_list.append("0")   # avg
        super().__init__(StudentRowData.total_key_list, input_string_list)

class IntRowData(RowData):
    #
    def __init__(self, title_text):
        row_list = [-1 for v in range(len(StudentRowData.input_key_list))]
        row_list[0] = title_text
        super().__init__(StudentRowData.input_key_list, row_list)

class TotalRowData(RowData):
    #
    def __init__(self, title_text):
        row_list = ["" for v in range(len(StudentRowData.total_key_list))]
        row_list[0] = title_text
        super().__init__(StudentRowData.total_key_list, row_list)

class StudentManager:
    #
    def __init__(self):
        self.__student_list = []
        self.__min_row = IntRowData("MIN")
        self.__max_row = IntRowData("MAX")
        self.__total_row = TotalRowData("TOTAL")
    #
    @staticmethod
    def check_name(name_string):
        if (len(name_string) < 1):
            return "이름을 입력해주세요!"
        return ""
    #
    @staticmethod
    def check_score(score_string):
        if (score_string.isdigit() == False):
            return "정수를 입력해주세요!"
        score = int(score_string)
        if ((score < 0) or (score > 100)):
            return "0점부터 100점 사이의 점수를 입력해주세요!"
        return ""
    #
    def print(self):
        line_width = RowData.cell_width * len(StudentRowData.title_list)
        print("-" * line_width)
        for title_text in StudentRowData.title_list:
            print(RowData.to_cell_string(title_text), end="")
        print()
        print("-" * line_width)
        for student_data in self.__student_list:
            student_data.print_screen()
        print("-" * line_width)
        self.__min_row.print_screen()
        self.__max_row.print_screen()
        print("-" * line_width)
        self.__total_row.print_screen()
        print("-" * line_width)
    #
    def load(self):
        path_file_list = __file__.split("\\")
        read_file = __file__.replace(path_file_list[-1], "student_score.txt")
        with open(read_file, "rt") as f:
            for line in f:
                read_value_list = line.strip().split()
                if (len(read_value_list) != len(StudentRowData.input_key_list)):
                    print("항목 개수 불일치! ({} != {})".format(len(read_value_list), len(StudentRowData.input_key_list)))
                    break
                self.__student_list.append(StudentRowData(read_value_list))
    #
    def calculate(self):
        total_sum = 0
        for student_data in self.__student_list:
            sum = 0
            for i in range(1, len(StudentRowData.input_key_list)):
                subject_key = StudentRowData.input_key_list[i]
                score_value = int(student_data.get_cell(subject_key))
                min_value = self.__min_row.get_cell(subject_key)
                if ((min_value == -1) or (min_value > score_value)):
                    self.__min_row.set_cell(subject_key, score_value)
                max_value = self.__max_row.get_cell(subject_key)
                if ((max_value == -1) or (max_value < score_value)):
                    self.__max_row.set_cell(subject_key, score_value)
                sum += score_value
            student_data.set_cell(StudentRowData.sum_key, str(sum))
            student_data.set_cell(StudentRowData.avg_key, str(sum / (len(StudentRowData.input_key_list) - 1)))
            total_sum += sum
        self.__total_row.set_cell(StudentRowData.sum_key, str(total_sum))
        self.__total_row.set_cell(StudentRowData.avg_key, str(total_sum / ((len(StudentRowData.input_key_list) - 1) * len(self.__student_list))))
    #
    def save(self):
        path_file_list = __file__.split("\\")
        write_file = __file__.replace(path_file_list[-1], "result.txt")
        with open(write_file, "wt") as f:
            line_width = RowData.cell_width * len(StudentRowData.title_list)
            for title_text in StudentRowData.title_list:
                f.write(RowData.to_cell_string(title_text))
            f.write("\n{}\n".format("-" * line_width))
            for student_data in self.__student_list:
                student_data.write_file(f)
            f.write("{}\n".format("-" * line_width))
            self.__min_row.write_file(f)
            self.__max_row.write_file(f)
            f.write("{}\n".format("-" * line_width))
            self.__total_row.write_file(f)

if (__name__ == "__main__"):
    try:
        print("# 시작")
        sm = StudentManager()
        while (True):
            print("1. 파일로부터 불러오기 (student_score.txt)")
            print("2. 계산하기 (합계, 평균, 최대, 최소)")
            print("3. 파일에 저장하기 (result.txt)")
            menu_no = input("메뉴 번호를 입력해주세요 : ")
            if (menu_no == "1"):
                sm.load()
                sm.print()
            elif (menu_no == "2"):
                sm.calculate()
                sm.print()
            elif (menu_no == "3"):
                sm.save()
                path_file_list = __file__.split("\\")
                write_file = __file__.replace(path_file_list[-1], "result.txt")
                os.system("notepad.exe " + write_file)
            else:
                print("잘못 입력하셨습니다!")
    except Exception as ex:
        print("# [NG] {} {}".format(type(ex), ex))
    else: # 예외가 발행하지 않을 때만 실행
        print("# [OK]")
    finally: # 예외 발생 여부와 관계없이 항상 실행
        print("# 종료")
        