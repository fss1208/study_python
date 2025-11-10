import sys

def test_io_file_read():
    print("# {}()".format(sys._getframe().f_code.co_name))
    fname = __file__.split("\\")[-1].replace(".py", ".txt")
    with open(fname, "rt") as f:
        for line in f:          # for line in f.readlines():
            print(line, end="") #   print(line.strip())

def test_io_file_write():
    print("# {}()".format(sys._getframe().f_code.co_name))
    fname = __file__.split("\\")[-1].replace(".py", ".txt")
    fmode = input("Please, input file mode? ")
    with open(fname, fmode) as f:
        for b in range(1,10):
            for a in range(2,10):
                f.write("{} x {} = {}\t".format(a, b, a*b))
            f.write("\n")

#########################################################    

if (__name__ == "__main__"):
    try:
        print("# 시작")
        while (True):
            print("-" * 30)
            print("1. test_io_file_read()")
            print("2. test_io_file_write()")
            menu = int(input("please, select menu? "))
            if (menu == 1): test_io_file_read()
            elif (menu == 2): test_io_file_write()
            else: break
    except Exception as ex:
        print("# [NG] {} {}".format(type(ex), ex))
    else: # 예외가 발행하지 않을 때만 실행
        print("# [OK]")
    finally: # 예외 발생 여부와 관계없이 항상 실행
        print("# 종료")
