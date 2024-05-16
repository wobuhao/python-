"""
函数的进阶
"""

# 1.函数多返回值

def test_return():
    return 1, 2
num1, num2 = test_return()
print(f"{num1}, {num2}")

# 2.函数多种传参方式
# a.位置参数 传递的参数和定义的参数的顺序及个数必须一致
def user_info(name, age, gender):
    print(f"{type(name)}, {type(age)}, {type(gender)}")
    print(f"您的名字是{name}, 年龄是{age}, 性别是{gender}")
user_info('Tom', 20, '男')

# b.关键字参数 函数调用时，如果有位置参数时，位置参数必须在关键字参数的前面，但关键字参数之间不存在先后顺序
def user_info(name, age, gender):
    print(f"您的名字是{name}, 年龄是{age}, 性别是{gender}")
name = '张飞'
user_info(name=name, age=2.5, gender="公")
user_info(age=2.5, gender="公", name="小咪")
user_info("小咪", age=2.5, gender="公")

# c.缺省参数 函数调用时，如果为缺省参数传值则修改默认参数值, 否则使用这个默认值
def user_info(name, age, gender='母'):
    print(f"您的名字是{name}, 年龄是{age}, 性别是{gender}")
user_info(name, 20) # 可以省略gender参数

# d.不定长参数 不定长参数也叫可变参数. 用于不确定调用的时候会传递多少个参数(不传参也可以)的场景
# 1).位置传递：传进的所有参数都会被args变量收集，它会根据传进参数的位置合并为一个元组(tuple)，args是元组类型
def user_info(*args):
    print(f"类型：{type(args)}，值：{args}")
user_info('小咪')
user_info('小咪', 18)

# 2).关键字传递：参数是“键=值”形式的形式的情况下, 所有的“键=值”都会被kwargs接受, 同时会根据“键=值”组成字典
def user_info(**kwargs):
    print(f"类型：{type(kwargs)}，值：{kwargs}")
user_info(name='黄小咪', age=18, id=110)

# 3.匿名函数
# a.函数作为参数传递
def compute(x, y):
    return x * y
def test_func(compute, nums):
    return compute(nums[0], nums[1])
print(f"函数作为参数传递:{test_func(compute, [2, 3])}")

# b.lambda匿名函数 无法二次使用
def test_func(compute, nums):
    print(compute(nums['first'], nums['second']))

test_func(lambda x, y: x**y, {'first': 2, 'second': 3})



