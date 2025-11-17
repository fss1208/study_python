import KSH

class TestClass:
    #
    object_count = 0
    #
    def __init__(self):
         self.public_value = "public"
         self._protected_value = "protected"
         self.__private_value = "private"
         TestClass.object_count += 1
    #
    @classmethod
    def print_classmethod_class_member(cls):
        print(cls.object_count)
    #
    @classmethod
    def set_classmethod_class_member(cls, count):
        cls.object_count = count
    #
    @staticmethod
    def print_staticmethod_class_member():
        print(TestClass.object_count)    
    #
    @staticmethod
    def set_staticmethod_class_member(count):
        TestClass.object_count = count    
    #
    @property
    def private_value(self):
        return self.__private_value
    #
    @private_value.setter
    def private_value(self, val):
        self.__private_value = val
    #
    def print(self):
        print(self.public_value, self._protected_value, self.__private_value, sep=",")

#########################################################    

@KSH.func_decorator
def test_private_member():
    tc = TestClass()
    tc.print()                                      # public,protected,private
    print(dir(tc))                                  # ['_TestClass__private_value', ... ]
    tc.public_value = "public member"   
    tc._protected_value = "protected member"    
    tc.__private_value = "private member"           # 맴버 변수가 추가로 생성되어 할당 (__private_value)
    print(dir(tc))                                  # ['_TestClass__private_value', '__private_value', ... ]
    tc.print()                                      # public member,protected member,private
    print(tc.__private_value)                       # private member (__private_value 변수 사용)
    tc.private_value = "asdf"                       # setter property 사용 : _TestClass__private_value 변수 사용
    tc.print()  
    print(tc.__private_value)                       # private member (__private_value 변수 사용)
    print(tc.private_value)                         # asdf (getter property 사용 : _TestClass__private_value 변수 사용)
    tc.aaaaaaaaa = "test"                           # 맴버 변수가 추가로 생성되어 할당 (aaaaaaaaa)
    print(tc.aaaaaaaaa)                             # test
    print(dir(tc))                                  # ['_TestClass__private_value', '__private_value', 'aaaaaaaaa', ... ]
    tc._TestClass__private_value = 123              # private으로 만들었지만 직접 접근 가능
    print(tc._TestClass__private_value)             # 123

@KSH.func_decorator
def test_class_static_method():
    print(dir(TestClass))   # [                             '__class__', ... , '__weakref__',                     'object_count', ... , 'private_value',                 'set_classmethod_class_member', 'set_staticmethod_class_member']
    TestClass.print_classmethod_class_member()      # 0
    TestClass.print_staticmethod_class_member()     # 0
    tc1 = TestClass()
    TestClass.print_classmethod_class_member()      # 1
    TestClass.print_staticmethod_class_member()     # 1
    print(dir(tc1))         # ['_TestClass__private_value', '__class__', ... , '__weakref__', '_protected_value', 'object_count', ... , 'private_value', 'public_value', 'set_classmethod_class_member', 'set_staticmethod_class_member']
    tc2 = TestClass()
    TestClass.print_classmethod_class_member()      # 2
    TestClass.print_staticmethod_class_member()     # 2
    print(dir(tc2))         # ['_TestClass__private_value', '__class__', ... , '__weakref__', '_protected_value', 'object_count', ... , 'private_value', 'public_value', 'set_classmethod_class_member', 'set_staticmethod_class_member']
    TestClass.set_classmethod_class_member(0)
    TestClass.print_classmethod_class_member()      # 0
    TestClass.set_staticmethod_class_member(999)
    TestClass.print_staticmethod_class_member()     # 999

#########################################################    

if (__name__ == "__main__"):
    try:
        print("# 시작")
        while (True):
            print("-" * 30)
            print("1. test_private_member()")
            print("2. test_class_static_method()")
            menu = int(input("please, select menu? "))
            if (menu == 1): test_private_member()
            elif (menu == 2): test_class_static_method()
            else: break
    except Exception as ex:
        print("# [NG] {} {}".format(type(ex), ex))
    else: # 예외가 발행하지 않을 때만 실행
        print("# [OK]")
    finally: # 예외 발생 여부와 관계없이 항상 실행
        print("# 종료")
