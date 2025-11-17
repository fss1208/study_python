import KSH
import pickle

pickle_file = "pickle.pbf"

@KSH.func_decorator
def test_io_file_write(pickle_data):
    print(pickle_data)
    # with open(pickle_file, "wt") as f:  # <class 'TypeError'> write() argument must be str, not bytes
    with open(pickle_file, "wb") as f:
        pickle.dump(pickle_data, f)

@KSH.func_decorator
def test_io_file_read():
    with open(pickle_file, "rb") as f:    
        pickle_data = pickle.load(f)
        print(pickle_data)

#########################################################    

if (__name__ == "__main__"):
    try:
        print("# 시작")
        while (True):
            print("-" * 30)
            print("1. test_io_file_write(list)")
            print("2. test_io_file_write(tuple)")
            print("3. test_io_file_write(set)")
            print("4. test_io_file_write(dict)")
            print("5. test_io_file_write(all)")
            print("11. test_io_file_read()")
            menu = int(input("please, select menu? "))
            if (menu == 1): test_io_file_write([1,"2",3.0])
            elif (menu == 2): test_io_file_write((1,"2",3.0))
            elif (menu == 3): test_io_file_write({1,"2",3.0})
            elif (menu == 4): test_io_file_write({"a":1,"b":"2","c":3.0})
            elif (menu == 5): test_io_file_write([1,("1",{"a":1,"b":{1,"2",3.0},"c":3.0},"3"),3.0])
            elif (menu == 11): test_io_file_read()
            else: break
    except Exception as ex:
        print("# [NG] {} {}".format(type(ex), ex))
    else: # 예외가 발행하지 않을 때만 실행
        print("# [OK]")
    finally: # 예외 발생 여부와 관계없이 항상 실행
        print("# 종료")
