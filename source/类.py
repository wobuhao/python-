"""
class 类
封装、继承、多态
"""
import json
from typing import Union
import random


class Person:
    # 如果构造方法中有赋值，可以省略
    name = None  # 成员属性
    age = None
    __hobby__ = None  # 私有属性 不能被类对象调用，但是可以给类成员使用

    # 构造方法 __init__ 构建类对象时会自动调用，一般用于给成员变量赋值
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        # 当类对象需要被转换为字符串的时候，会调用此方法
        return "调用__str__"  # 返回值为 str

    # 小于符号比较 < 两个对象进行比较时，会调用此方法，如果没有实现此方法，对象比较会报错
    def __lt__(self, other):
        return self.age < other.age  # 返回值为 True或False

    # 小于等于符号比较 <=、>=
    def __le__(self, other):
        return self.age <= other.age  # 返回值为 True或False

    # 等于符号比较 ==
    def __eq__(self, other):
        return self.age == other.age  # 返回值为 True或False

    # 成员方法 在方法内部，想要访问类的成员变量，必须使用self,self传参时可以忽略
    def say_hi(self):
        print(f"你好，我是{self.name}")

    # 私有方法 不能被类对象调用，但是可以给类成员使用
    def __run(self):
        print(f"私有方法")


s1 = Person('勇哥', '30')
s1.name = '勇哥2'
s1.say_hi()
print(f"{s1}")


# 继承 单继承和多继承 多个父类中，如果有同名的成员，那么默认以继承顺序(从左到右)为优先级
# 即：先继承的保留，后继承的被覆盖
class Student(Person):
    pass

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def say_hi(self):
        # 调用父类方法 两种方式
        Person.say_hi(self)
        print(f"{Person.name}")
        super().say_hi()
        print(f"{super().name}")
        print(f"这是Student类的say_hi方法，{self.name}")


s2 = Student(name='小白', age=20, address="日本市")
s2.say_hi()

# 类型注解
# 基础数据类型注解


v1: int = 10
v2: str = "aaa"
v3: bool = True


# 类对象类型注解
class Student:
    pass


stu: Student = Student()

# 基础容器类型注解
mylist: list = [1, 2, 3]
mytuple: tuple = (1, 2, 3)
mydict: dict = {"abc": 123}

# 容器类型详细注解
mylist: list[int] = [1, 2, 3]
mytuple: tuple[int] = (1, 2, 3)
mydict: dict[str, int] = {"abc": 123}

# 在注释中进行类型注解
v4 = random.randint(1, 10)  # type: int


# v5 = json.loads("{'name' : 'zhangsan'}")  # type: dict

# 函数注解
def add(x: int, y: int) -> int:
    return x + y


# Union类型
my_list1: list[Union[str, int]] = ['aa', 1, 2]

my_dict1: dict[str, Union[int, str]] = {"name": "hy", "age": 18}


def get_data(data: Union[str, int]) -> Union[str, int]:
    return data


# 多态
class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("汪汪汪")


class Cat(Animal):
    def speak(self):
        print("喵喵喵")


def make_noise(animal: Animal):
    animal.speak()


dog = Dog()
cat = Cat()
make_noise(dog)
make_noise(cat)
