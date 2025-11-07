import sys

def test_string():
    print("# {}()".format(sys._getframe().f_code.co_name))
    p = "python"
    print("'python'")               # 'python'
    print('"python"')               # "python"
    print('''"""python"""''')       # """python"""
    print("""'''python'''""")       # '''python'''
    print("Hello " + "python")      # Hello python
    print("python " * 3)            # python python python
    for ch in p:
        print(ch, end=" ")          # p y t h o n
    print()
    for i in range(0,len(p)):
        print(p[-1-i], end=" ")     # n o h t y p
    print()

def test_string_escape_sequence():
    print("# {}()".format(sys._getframe().f_code.co_name))
    print("1st \t 2nd")             # 1st      2nd
    print("1st \n 2nd")             # 1st \n 2nd
    print("1st \r 2nd")             # 커서의 위치를 같은 행의 맨 앞으로 이동
    print("1st \b 2nd")             # 커서의 위치를 왼쪽으로 한 칸 이동
    print("1st \a 2nd")             # beep
    print('I\'m \'progammer\'.')    # I'm 'progammer'.
    print("I'm \"programmer\".")    # I'm "programmer".
    print("\101")                   # A : 8진수 아스키 코드에 해당하는 문자 출력
    print("\x41")                   # A : 16진수 아스키 코드에 해당하는 문자 출력

def test_string_slicing():
    print("# {}()".format(sys._getframe().f_code.co_name))
    s = "Python"
    print(s)                        # Python
    print(s[::-1])                  # nohtyP
    print(s[-1::-1])                # nohtyP
    print(s[-1:0:-1])               # nohty
    print(s[::-2])                  # nhy
    print(s[1:1])                   # 빈문자열 출력
    print(s[4:2])                   # 빈문자열 출력

def test_string_operating():
    print("# {}()".format(sys._getframe().f_code.co_name))
    p = "python"
    # in #################################################
    print("p" in p)                 # True
    print("py" in p)                # True
    print("python" in p)            # True
    print("Python" in p)            # False
    # 비교연산자 ###########################################
    print("a" < "b")                # True
    print("a" == "A")               # False
    print("a" > "A")                # True
    print("apple" < "Banana")       # False
    print("apple" < "banana")       # True
    print("dict" < "dictionary")    # True
    print(" " < "1" < "A" < "a")    # True
    print("' ' = %d" % ord(" "))    # ' ' = 32
    print("'1' = %d" % ord("1"))    # '1' = 49
    print("'A' = %d" % ord("A"))    # 'A' = 65
    print("'a' = %d" % ord("a"))    # 'a' = 97

def test_string_formmating():
    print("# {}()".format(sys._getframe().f_code.co_name))
    vi, vf, vs = 255, 3.141592, "α + β"
    print("%d" % vi)                                        # 255
    print("%i" % vi)                                        # 255
    print("%o" % vi)                                        # 377
    print("%x" % vi)                                        # ff
    print("%X" % vi)                                        # FF
    print("%f" % vf)                                        # 3.141592
    print("%F" % vf)                                        # 3.141592
    print("%e" % vf)                                        # 3.141592e+00
    print("%E" % vf)                                        # 3.141592E+00
    print("%g" % 0.0003)                                    # 0.0003
    print("%g" % 0.00003)                                   # 3e-05
    print("%G" % 0.0003)                                    # 0.0003
    print("%G" % 0.00003)                                   # 3E-05
    print("%s" % vs)                                        # α + β : str() 함수를 사용한 것과 동일
    print("%r" % vs)                                        # 'α + β' : repr() 함수를 사용한 것과 동일
    print("%a" % vs)                                        # '\u03b1 + \u03b2' : ascii() 함수를 사용한 것과 동일
    print("77%%")                                           # 77%%
    print("77%")                                            # 77%
    print("%c" % "z")                                       # z
    print("{}\t{}\t{}".format(vi, vf, vs))                  # 255     3.141592    α + β
    print("{2}\t{0}\t{0}".format(vi, vf, vs))               # α + β   255     255
    print("{ii}\t{ff}\t{ss}".format(ss=vs, ii=vi, ff=vf))   # 255     3.141592    α + β
    print("{0:.2f}".format(vf))                             # 3.14
    print("%c" % "xyz")                                     # <class 'TypeError'> %c requires int or char

def test_string_method():
    print("# {}()".format(sys._getframe().f_code.co_name))
    no_str = "012345"
    lo_str = "python"
    up_str = "PYTHON"
    st_str = "   python   "
    temp, beta = "AbcDEFghi", "β"
    print("%s >> %s" % (lo_str, lo_str.upper()))                    # python >> PYTHON
    print("%s >> %s" % (up_str, up_str.lower()))                    # PYTHON >> python
    print("%s >> %s" % (lo_str, lo_str.capitalize()))               # python >> Python
    print("%s >> %s" % (up_str, up_str.capitalize()))               # PYTHON >> Python
    print("%s >> %s" % (temp, temp.casefold()))                     # AbcDEFghi >> abcdefghi
    print("%s >> %s" % (beta, beta.casefold()))                     # β >> β
    print(lo_str.center(12,"*"))                                    # ***python***
    print("0113336666633".count("3"))                               # 5
    print("0113336666633".count("3",5))                             # 3
    print("0113336666633".count("3",5,11))                          # 1 :  start_index <= 범위 < end_index
    print(lo_str.endswith("on"))                                    # True
    print(lo_str.endswith("hon"))                                   # True
    print(lo_str.endswith("ho"))                                    # False
    print(lo_str.endswith("tho", 0, 5))                             # True
    print("a,bb,ccc".split(","))                                    # ["a", "bb", "ccc"]
    print(",".join(["a", "bb", "ccc"]))                             # a,bb,ccc
    print("-".join(no_str))                                         # 0-1-2-3-4-5
    print(no_str.join("-"))                                         # -
    lst = list(lo_str)
    print("{} >> {}".format(lst, "".join(lst)))                     # ['p', 'y', 't', 'h', 'o', 'n'] >> python
    print("{} ({})".format(st_str.strip(), len(st_str.strip())))    # python (6)
    print("{} ({})".format(st_str.rstrip(), len(st_str.rstrip())))  #    python (9)
    print("{} ({})".format(st_str.lstrip(), len(st_str.lstrip())))  # python    (9)
    print(no_str.index("23"))                                       # 2
    print(no_str.index("23", 2))                                    # 2
    print(no_str.index("23", 2, 3))                                 # [NG] <class 'ValueError'> substring not found
    print(no_str.index("23", 3))                                    # [NG] <class 'ValueError'> substring not found
    print(no_str.index("xx"))                                       # [NG] <class 'ValueError'> substring not found

###########################################################    

if (__name__ == "__main__"):
    try:
        print("# 시작")
        while (True):
            print("-" * 30)
            print("1. test_string()")
            print("2. test_string_escape_sequence()")
            print("3. test_string_slicing()")
            print("4. test_string_operating()")
            print("5. test_string_formmating()")
            print("6. test_string_method()")
            menu = int(input("please, select menu? "))
            if (menu == 1): test_string()
            elif (menu == 2): test_string_escape_sequence()
            elif (menu == 3): test_string_slicing()
            elif (menu == 4): test_string_operating()
            elif (menu == 5): test_string_formmating()
            elif (menu == 6): test_string_method()
            else: break
    except Exception as ex:
        print("# [NG] {} {}".format(type(ex), ex))
    else: # 예외가 발행하지 않을 때만 실행
        print("# [OK]")
    finally: # 예외 발생 여부와 관계없이 항상 실행
        print("# 종료")
