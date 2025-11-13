import sys
import KSH

def test_string():
    print("# {}()".format(sys._getframe().f_code.co_name))
    p = "python"
    print("'python'")               # 'python'
    print('"python"')               # "python"
    print('''"""python"""''')       # """python"""
    print("""'''python'''""")       # '''python'''
    print("Hello " + "python")      # Hello python
    print("python " * 3)            # python python python
    print(type(p[0]))               # <class 'str'>
    print(type(p))                  # <class 'str'>
    print(len(p))                   # 6
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
    print("%10s." % vs)                                     #      α + β.
    print("%-10s." % vs)                                    # α + β     .     
    print("{}\t{}\t{}".format(vi, vf, vs))                  # 255     3.141592    α + β
    print("{2}\t{0}\t{0}".format(vi, vf, vs))               # α + β   255     255
    print("{ii}\t{ff}\t{ss}".format(ss=vs, ii=vi, ff=vf))   # 255     3.141592    α + β
    print("{0:.2f}".format(vf))                             # 3.14 : 0.2f와 같음
    print("{0:10.2f}".format(vf))                           #       3.14
    print("{0:>10}".format("test"))                         #       test
    print("{0:-^10}".format("test"))                        # ---test---
    print("{0:^10}".format("test"))                         #    test
    print("{0:=^10}".format("test"))                        # ===test===
    print("{0:<10}".format("test"))                         # test      
    print("{{name}}".format())                              # {name}
    print("{0:4d}".format(7))                               #    7
    print("{0:04d}".format(7))                              # 0007
    print("{0:<4}".format(7))                               # 7
    print("{0:,}".format(123456789))                        # 123,456,789
    print("{0:.2f}".format(3.141592))                       # 3.14
    print("{0:.2%}".format(0.12345))                        # 12.35%
    print("{0:.2e}".format(9253000))                        # 9.25e+06
    print("{0:#x}".format(255))                             # 0xff
    print("{0:x}".format(255))                              # ff
    print("{0:#o}".format(8))                               # 0o10
    print("{0:o}".format(8))                                # 10
    print("{0:#b}".format(2))                               # 0b10
    print("{0:b}".format(2))                                # 10
    name, age = "KSH", 77   
    print(f"이름:{name}, 나이:{age}")                        # 이름:KSH, 나이:77 (python 3.6 버전부터 사용 가능)
    print("%d%%" % 77)                                      # 77%
    print("%d%" % 77)                                       # <class 'ValueError'> incomplete format
    print("%c" % "z")                                       # z
    print("%c" % "xyz")                                     # <class 'TypeError'> %c requires int or char

def test_string_method():
    print("# {}()".format(sys._getframe().f_code.co_name))
    no_str = "012345"
    lo_str = "python"
    up_str = "PYTHON"
    st_str = "   python   "
    temp, beta = "AbcDEFghi", "β"
    print("# upper() : 전체 문자열을 대문자로 변환")
    print("%s >> %s" % (lo_str, lo_str.upper()))                    # python >> PYTHON
    print("# lower() : 전체 문자열을 소문자로 변환")
    print("%s >> %s" % (up_str, up_str.lower()))                    # PYTHON >> python
    print("# capitalize() : 첫문자는 대문자로 나머지는 소문자로 변환")
    print("%s >> %s" % (lo_str, lo_str.capitalize()))               # python >> Python
    print("%s >> %s" % (up_str, up_str.capitalize()))               # PYTHON >> Python
    print("# casefold() : 비교 판단 가능한 문자열로 변환")
    print("%s >> %s" % (temp, temp.casefold()))                     # AbcDEFghi >> abcdefghi
    print("%s >> %s" % (beta, beta.casefold()))                     # β >> β
    print("# center(반복회수, '반복문자열')")
    print(lo_str.center(12,"*"))                                    # ***python***
    print("# count('카운팅문자열', start_index=0, end_index=문자열길이)")
    print("0113336666633".count("3"))                               # 5
    print("0113336666633".count("3",5))                             # 3
    print("0113336666633".count("3",5,11))                          # 1 :  start_index <= 범위 < end_index
    print("# find('찾을문자열', start_index=0, end_index=문자열길이)")
    print(lo_str.find("tho"))                                       # 2
    print(lo_str.find("tho", 3))                                    # -1 : start_index(3)에서 끝까지
    print(lo_str.find("tho", 2, 4))                                 # -1 : start_index(2) <= 범위 < end_index(4)
    print(lo_str.find("t"))                                         # 2
    print(up_str.find("t"))                                         # -1
    print("# replace('old','new',count=-1) : count를 지정하지 않으면 전체를 바꾸고 지정하면 해당 횟수만큼 왼쪽에서 부터 바꿈")
    print("%s >> %s" % (up_str, up_str.replace("YTHO", "ytho")))    # PYTHON >> PythoN
    print("%s >> %s" % (lo_str, lo_str.replace("YTHO", "ytho")))    # python >> python
    print("abbcccddddcccbbabbccccdddd".replace("bb", "BB"))         # aBBcccddddcccBBaBBccccdddd
    print("abbcccddddcccbbabbccccdddd".replace("bb", "BB", 2))      # aBBcccddddcccBBabbccccdddd
    print("# isdigit() : 문자열이 모두 숫자로 구성되어 있을 때만 True")
    print("123".isdigit())                                          # True
    print("12a".isdigit())                                          # False : 문자 포함
    print("1 3".isdigit())                                          # False : 공백 포함
    print("# isalpha() : 문자열이 숫자,특수문자,공백이 아닌 문자로 구성되어 있을 때만 True")
    print("abc".isalpha())                                          # True
    print("ab1".isalpha())                                          # False
    print("a c".isalpha())                                          # False
    print("# isalnum() : 문자열이 특수문자,공백이 아닌 문자와 숫자로 구성되어 있을 때만 True")
    print("Python1".isalnum())                                      # True
    print("Python1 ".isalnum())                                     # False
    print("Python1\t".isalnum())                                    # False
    print("# isspace() : 문자열이 모두 공백 문자로 구성되어 있을 때만 True")
    print("     ".isspace())                                        # True
    print("\t".isspace())                                           # True
    print("\n".isspace())                                           # True
    print("\n \t".isspace())                                        # True
    print("\n \t.".isspace())                                       # False
    print("# isupper() : 문자열이 모두 대문자로 구성되어 있을 때만 True")
    print("ABC".isupper())                                          # True
    print("AbC".isupper())                                          # False
    print("# islower() : 문자열이 모두 소문자로 구성되어 있을 때만 True")
    print("abc".islower())                                          # True
    print("aBc".islower())                                          # False
    print("# startswith('찾을문자열', start_index=0, end_index=문자열길이)")
    print(lo_str.startswith("py"))                                  # True
    print(lo_str.startswith("th"))                                  # False
    print(lo_str.startswith("th",2))                                # True : start_index(2)에서 끝까지
    print(lo_str.startswith("th",2,3))                              # False : start_index(2) <= 범위 < end_index(3)
    print("# endswith('찾을문자열', start_index=0, end_index=문자열길이)")
    print(lo_str.endswith("on"))                                    # True
    print(lo_str.endswith("ho"))                                    # False
    print(lo_str.endswith("ho", 3))                                 # False : start_index(3)에서 끝까지
    print(lo_str.endswith("ho", 1, 5))                              # True : start_index(1) <= 범위 < end_index(5)
    print("# split('구분문자열', 최대구분횟수)")
    print("a,bb,ccc".split(","))                                    # ["a", "bb", "ccc"]
    print("a,bb,ccc".split(",",maxsplit=1))                         # ['a', 'bb,ccc']
    print("a,bb,ccc".split(",",maxsplit=9))                         # ['a', 'bb', 'ccc']
    print("a,bb,ccc".split(",",maxsplit=0))                         # ['a,bb,ccc']
    print("+82-01-2345-6789".split("-",maxsplit=1))                 # ['+82', '01-2345-6789']
    print("+82-01-2345-6789".split("2-0"))                          # ['+8', '1-2345-6789']
    print("+82-01-2345-6789".split("A"))                            # ['+82-01-2345-6789']
    print("  abc \t def \t\t\n ghi ".split(" "))                    # ['', '', 'abc', '\t', 'def', '\t\t', 'ghi', '']
    print("  abc \t def \t\t\n ghi ".split("\t"))                   # ['  abc ', ' def ', '', ' ghi ']
    print("  abc \t def \t\t\n ghi ".split())                       # ['abc', 'def', 'ghi']
    print("# join 함수")
    print(",".join(["a", "bb", "ccc"]))                             # a,bb,ccc
    print("-".join(no_str))                                         # 0-1-2-3-4-5
    print(no_str.join("-"))                                         # -
    lst = list(lo_str)
    print("{} >> {}".format(lst, "".join(lst)))                     # ['p', 'y', 't', 'h', 'o', 'n'] >> python
    print("# strip 함수 : 문자열 앞과 뒤의 모든 공백과 개행문자를 삭제")   # ' '과 '\n' 문자 제거
    print("{} ({})".format(st_str, len(st_str)))                    #    python    (12)
    print("{} ({})".format(st_str.strip(), len(st_str.strip())))    # python (6)
    print("{} ({})".format(st_str.rstrip(), len(st_str.rstrip())))  #    python (9)
    print("{} ({})".format(st_str.lstrip(), len(st_str.lstrip())))  # python    (9)
    print("aaaPythonaaa >> {}".format("aaaPythonaaa".strip("a")))   # aaaPythonaaa >> Python
    print("aaaPythonaaa >> {}".format("aaaPythonaaa".strip("Pan"))) # aaaPythonaaa >> ytho
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
