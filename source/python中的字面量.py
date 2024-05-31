
import  random
# 单行注释

"""
    多行注释
"""

123
12.12
"你好"
print('你好')
print(123)
print(123.123)

# 变量
name = 'hy'
name = "hyhy"
name = "\"你好" # 可以使用 \ 进行转义
name = """
hy
hy
"""
money = 50
print("钱包余额还有:", money)

# 数据类型 int float str

# type() 方法可以输出变量的类型
print(type(money))
print(type('你好'))

print(int("1"))

# 数据类型互转
str1 = str(1)
str2 = int(str1)
str3 = float(str2)

print(str1, str2, str3)

# Python 关键字
"""
False True None and as assert break class
continue def del elif else except finally for 
from global if import in is lambda nonlocal 
not or pass raise return try while with yield
"""

# 运算符
"""
算术运算符
+ 加 
- 减
* 乘
/ 除
// 取整除
% 取余
** 指数

赋值运算符
=

复合赋值运算符
+=  c += a 等效于 c = c + a
-=  c -= a 等效于 c = c - a
*=  c *= a 等效于 c = c * a
/=  c /= a 等效于 c = c / a
%=  c %= a 等效于 c = c % a
**= c **= a 等效于 c = c ** a
//= c //= a 等效于 c = c // a
"""

# 字符串拼接 +  %s 可占位字符串 %d 可占位整数 %f 可占位浮点数 控制精度 %.2f %3.2f
name = 'huang' + 'yong'
nameStr = "你是谁 %s" % (name)
print(nameStr)
print(f"我是{name}")
print('数据类型是%s' % type(name))
# 注意，使用+只能拼接字符串不能拼接 int， float

num = random.randint(1, 10)
print(num)
getStr = int(input("请告诉我，你猜的数字是？"))
count = 0;
while getStr != num:
    count += 1
    print(f"整错了哈 {getStr}")
    getStr = int(input("请继续猜吧!"))

print("回答正确：%s, 一共回答： %d 次" % (getStr, count), end='')
print('hahaha')
print('a\t对齐')
print('bbc\t对齐')
# if getStr == num:
#     print("回答正确：%s" % getStr)
# else:
#     print(f"整错了哈 {getStr}")

# 九九乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j}*{i}={i*j}\t", end='')
        j += 1
    i += 1
    print('')

for x in nameStr:
    print(x)

for y in range(5):
    print(y)

# break 结束循环 continue 结束本次循环
for x in range(1, 10):
    if x == 5:
        break
    for z in range(1, x+1):
        print(f"{z}*{x}={z*x}\t", end='')
    print()

# 函数的定义
def get_name(name, age):
    """
    处理姓名函数
    :param name:姓名
    :param age:年龄
    :return: None
    """
    print("你好：%s" % nameStr)
    return None

if not get_name(nameStr, 1):
    print('hah')

# 函数默认的返回值是 None None字面量可用于 函数返回值、if判断、变量定义
# 定义全局类型 global 可在函数中定义全局变量


