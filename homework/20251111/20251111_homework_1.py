# 과목별 점수 입력 함수
def input_subject_score(sub_title):
    while (True):
        temp = input("{} 점수를 입력해주세요 (0 ~ 100) : ".format(sub_title))
        if (temp.isdigit() == False):
            print("정수를 입력해주세요!")
            continue
        score = int(temp)
        if ((score < 0) or (score > 100)):
            print("0점부터 100점 사이의 점수를 입력해주세요!")
            continue
        return score

# 입력 및 계산
students = 5    # 학생수
total_sum = 0   # 전체 합계
total_avg = 0   # 전체 평균
name_key, kor_key, mat_key, eng_key, sci_key, sum_key, avg_key = "name", "kor", "mat", "eng", "sci", "sum", "avg"
title_dict = {name_key:"이름", kor_key:"국어", mat_key:"수학", eng_key:"영어", sci_key:"과학", sum_key:"합계", avg_key:"평균"}
min_dict = {kor_key:-1, mat_key:-1, eng_key:-1, sci_key:-1}     # 과목별 최소값
max_dict = {kor_key:-1, mat_key:-1, eng_key:-1, sci_key:-1}     # 과목별 최대값
subject_key_list = [kor_key, mat_key, eng_key, sci_key]         # 과목 키값 리스트
student_score_list = []
dash_cnt = 52    
for i in range(students):
    score_dict = dict()
    sum = 0
    # 이름 입력
    while (True):
        name = input("{}. {} : ".format(i+1, title_dict[name_key]))
        if (len(name) < 1):
            print("이름을 입력해주세요!")
            continue
        score_dict[name_key] = name
        break
    # 과목별 점수 입력 및 계산
    for sub_key in subject_key_list:
        score = input_subject_score("{}. {}".format(i+1, title_dict[sub_key]))
        score_dict[sub_key] = score
        if (min_dict[sub_key] == -1) or (min_dict[sub_key] > score):
            min_dict[sub_key] = score
        if (max_dict[sub_key] == -1) or (max_dict[sub_key] < score):
            max_dict[sub_key] = score
        sum += score
    score_dict[sum_key] = sum
    score_dict[avg_key] = sum / len(subject_key_list)
    total_sum += sum
    student_score_list.append(score_dict)
total_avg = total_sum / (students * len(subject_key_list))
# 출력
print("-" * dash_cnt)
for title_key in title_dict.keys():
    print(title_dict[title_key], end="\t")
print()
print("-" * dash_cnt)
for score_dict in student_score_list:
    for sub_key in score_dict.keys():
        print(score_dict[sub_key], end="\t")
    print()
print("-" * dash_cnt)
print("최소", end="\t")
for sub_key in min_dict.keys():
    print(min_dict[sub_key], end="\t")
print()
print("최대", end="\t")
for sub_key in max_dict.keys():
    print(max_dict[sub_key], end="\t")
print()
print("-" * dash_cnt)
print("전체\t\t\t\t\t{}\t{}".format(total_sum, total_avg))
print("-" * dash_cnt)
