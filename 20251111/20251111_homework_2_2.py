# 파일을 읽어와 학생에 따른 점수의 평균 및 전체평균, 과목별 최대 및 최소점수 계산
students = 0    # 학생수
total_sum = 0   # 전체 합계
total_avg = 0   # 전체 평균
name_key, kor_key, mat_key, eng_key, sci_key, sum_key, avg_key = "name", "kor", "mat", "eng", "sci", "sum", "avg"
title_dict = {name_key:"NAME", kor_key:"KOREAN", mat_key:"MATH", eng_key:"ENGLISH", sci_key:"SCIENCE", sum_key:"SUM", avg_key:"AVERAGE"}
min_dict = {kor_key:-1, mat_key:-1, eng_key:-1, sci_key:-1}     # 과목별 최소값
max_dict = {kor_key:-1, mat_key:-1, eng_key:-1, sci_key:-1}     # 과목별 최대값
subject_key_list = [kor_key, mat_key, eng_key, sci_key]
read_column_count = len(subject_key_list) + 1
student_score_list = []
path_file_list = __file__.split("\\")
score_file = __file__.replace(path_file_list[-1], "student_score.txt")
with open(score_file, "rt") as f:
    for line in f:
        read_value_list = line.strip().split("\t")
        if (len(read_value_list) != read_column_count):
            print("항목 개수 불일치! ({} != {})".format(len(read_value_list), read_column_count))
            break
        sum = 0
        read_student_dict = dict()
        read_student_dict[name_key] = read_value_list[0]
        # 과목별 점수 입력 및 계산
        for i in range(len(subject_key_list)):
            read_key = subject_key_list[i]
            read_value = int(read_value_list[i+1])
            read_student_dict[read_key] = read_value
            if (min_dict[read_key] == -1) or (min_dict[read_key] > read_value):
                min_dict[read_key] = read_value
            if (max_dict[read_key] == -1) or (max_dict[read_key] < read_value):
                max_dict[read_key] = read_value
            sum += read_value
        read_student_dict[sum_key] = sum
        read_student_dict[avg_key] = sum / len(subject_key_list)
        total_sum += sum
        students += 1
        student_score_list.append(read_student_dict)
total_avg = total_sum / (students * len(subject_key_list))
# 파일에 저장
cell_width = 10
dash_count = len(title_dict) * cell_width
result_file = __file__.replace(path_file_list[-1], "result.txt")
with open(result_file, "wt") as f:
    for k, v in title_dict.items():
        f.write(v.center(cell_width))
    f.write("\n" + "-" * dash_count + "\n")
    for score_dict in student_score_list:
        for k, v in score_dict.items():
            f.write(str(v).center(cell_width))
        f.write("\n")
    f.write("-" * dash_count)
    f.write("\n" + "MIN".center(cell_width))
    for k, v in min_dict.items():
        f.write(str(v).center(cell_width))
    f.write("\n" + "MAX".center(cell_width))
    for k, v in max_dict.items():
        f.write(str(v).center(cell_width))
    f.write("\n" + "-" * dash_count)
    f.write("\n{}{}{}{}".format("TOTAL".center(cell_width), " " * 40, str(total_sum).center(cell_width), str(total_avg).center(cell_width)))