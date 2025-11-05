import sys

def test_dictinoary():
    print("# {}()".format(sys._getframe().f_code.co_name))
    dct = {"a":1, "b":2, "c":3}
    print(type(dct))                        # <class 'dict'>  
    print(dct)                              # {'a': 1, 'b': 2, 'c': 3}
    print(dct.keys())                       # dict_keys(['a', 'b', 'c'])
    print(dct.values())                     # dict_values([1, 2, 3])
    print(dct.items())                      # dict_items([('a', 1), ('b', 2), ('c', 3)])
    test_dictionary_info(dct)
    dct["a"] = 11
    print(dct)                              # {'a': 11, 'b': 2, 'c': 3}
    dct["d"] = 4
    print(dct)                              # {'a': 11, 'b': 2, 'c': 3, 'd': 4}
    del dct["d"]
    print(dct)                              # {'a': 11, 'b': 2, 'c': 3}
    dct.clear()
    print(dct)                              # {}
    dct1 = {"A":"SeSAC", "B":"ChatGPT"}
    dct2 = {"C":"AI", "B":"Python"}
    dct.update(dct1)
    print(dct1)                             # {'A': 'SeSAC', 'B': 'ChatGPT'}
    print(dct2)                             # {'C': 'AI', 'B': 'Python'}
    print(dct)                              # {'A': 'SeSAC', 'B': 'ChatGPT'}
    del dct["e"]                            # <class 'KeyError'> 'e'

def test_dictionary_info(dct):
    for key in dct.keys():
        print("{} {}".format(type(key), key))
    for value in dct.values():
        print("{} {}".format(type(value), value))
    for item in dct.items():
        print("{} {}".format(type(item), item))

#########################################################    

if (__name__ == "__main__"):
    try:
        print("# 시작")
        test_dictinoary()
    except Exception as ex:
        print("{} {}".format(type(ex), ex))
    else: # 예외가 발행하지 않을 때만 실행
        print("# 처리 완료")
    finally: # 예외 발생 여부와 관계없이 항상 실행
        print("# 종료")
