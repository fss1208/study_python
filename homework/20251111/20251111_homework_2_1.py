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

# 5명의 학생 데이터 입력
students = 5    # 학생수
name_key, kor_key, mat_key, eng_key, sci_key = "name", "kor", "mat", "eng", "sci"
title_dict = {name_key:"이름", kor_key:"국어", mat_key:"수학", eng_key:"영어", sci_key:"과학"}
subject_key_list = [kor_key, mat_key, eng_key, sci_key]
student_score_list = []
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
    for sub_key in subject_key_list:
        score = input_subject_score("{}. {}".format(i+1, title_dict[sub_key]))
        score_dict[sub_key] = score
    student_score_list.append(score_dict)
# 파일 기록
path_file_list = __file__.split("\\")
score_file = __file__.replace(path_file_list[-1], "student_score.txt")
with open(score_file, "wt") as f:
    for score_dict in student_score_list:
        for k, v in score_dict.items():
            f.write("{}\t".format(v))
        f.write("\n")
