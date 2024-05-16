"""
异常、模块与包
"""
# 异常处理 捕获常规异常
try:
    f = open('haha.txt', 'r')
except:
    f = open('haha.txt', 'w')

# 捕获单个或者多个异常
try:
    print(name)
except (NameError, ZeroDivisionError) as e:
    print(e)

# 捕获所有异常
try:
    print(1/0)
except Exception as e:
    print(e)

# 异常else
try:
    print(1)
except Exception as e:
    print(e)
else:
    print('正常执行吧')

# 异常的finally 无论如何都要执行的代码
try:
    f = open('haha.txt', 'r')
except Exception as e:
    print(f"发生异常{e}")
    f = open('haha.txt', 'w')
else:
    print('无异常')
finally:
    f.close()

# 异常的传递
def funco1():
    num = 1 / 0

def funco2():
    funco1()

def main():
    try:
        funco2()
    except Exception as e:
        print(f"main函数中捕获异常：{e}")

main()

# Module 模块导入方式如下,写在代码开头位置, 不同模块，同名的功能，如果都被导入，那么后导入的会覆盖先导入的
# a. import 模块名
import time
time.sleep(1)
print('hello')

# b. from 模块名 import 类、变量、方法等
from time import sleep
sleep(1)
print('hello')

# c. from 模块名 import *
from time import *
sleep(1)
print('hello')

# d. import 模块名 as 别名
import time as tt
tt.sleep(1)
print('hello')

# e. from 模块名 import 功能名 as 别名
from time import sleep as sl
sl(1)
print('hello')

# Module 自定义模块
from my_module import test
test(a=1, b=2)

from my_module_all import *
test_a()

# 包

# 自定义包
from my_package import test_m,test_a
print(f"{test_a.sum()}")

