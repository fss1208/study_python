import sys

def test_if():
    print("# {}()".format(sys._getframe().f_code.co_name))
    x = int(input())
    if (x >= 100):
        print("good")
    elif ((x >= 60) and (x < 100)):
        print("pass")
    else:
        print("fail")

def test_for():
    print("# {}()".format(sys._getframe().f_code.co_name))
    print(list(range(0,5,1)))       # [0, 1, 2, 3, 4]
    print(list(range(0,5)))         # [0, 1, 2, 3, 4]
    print(list(range(5)))           # [0, 1, 2, 3, 4]
    for i in range(1,10):
        for j in range(1,10):
            print("{} x {} = {}".format(i, j, i*j), end='\t')   # i x j = k
        print()
    lst1 = [i for i in range(1,10) if i%2!=0]
    lst2 = [i for i in range(1,10) if i%2==0]
    print(lst1) # [1, 3, 5, 7, 9]
    print(lst2) # [2, 4, 6, 8]
    for a,b in zip(lst1,lst2): # 4번 반복
        print("{} {}".format(a,b), end=" : ") # 1 2 : 3 4 : 5 6 : 7 8 :
    print()
    for a,b in zip(lst2,lst1): # 4번 반복
        print("{} {}".format(a,b), end=" : ") # 2 1 : 4 3 : 6 5 : 8 7 :
    print()

def test_while():
    print("# {}()".format(sys._getframe().f_code.co_name))
    while (True):
        pw = input("비밀번호를 입력하세요 : ")
        if (pw == "1411"):
            break

#########################################################    

if (__name__ == "__main__"):
    try:
        print("# 시작")
        test_while()
    except Exception as ex:
        print("{} {}".format(type(ex), ex))
    else: # 예외가 발행하지 않을 때만 실행
        print("# 처리 완료")
    finally: # 예외 발생 여부와 관계없이 항상 실행
        print("# 종료")
