"""
文件操作
"""

# 文件的编码
# a.编码就是一种规则集合，记录了内容和二进制间进行相互转换的逻辑。
# b.编码有许多中，我们最常用的是UTF-8编码

# 文件的读取
"""
open(name, mode, encoding)
name：是要打开的目标文件名的字符串(可以包含文件所在的具体路径)。
mode：设置打开文件的模式(访问模式)：只读、写入、追加等。r:读 w:写，如果文件不存在，会创建新文件进行写入 a:追加内容,如果文件不存在，会创建新文件进行写入
encoding:编码格式（推荐使用UTF-8）
"""
f = open('data.txt', 'r')
# 文件对象.read(num) num:表示要从文件中读取的数据的长度（单位是字节），如果没有传入num，那么就表示读取文件中所有的数据
# print(f"read:\n{f.read()}")

# 文件对象.readlines() 可以按照行的方式把整个文件中的内容进行一次性读取，并且返回的是一个列表，其中每一行的数据为一个元素。
print(f"readlines:\t{f.readlines()}")
# content = f.readline()
# print(f"readline:\n{content}")

# for循环读取文件行
for x in open('data.txt', 'r'):
    print(f":{x}")

# with open 语法
# with open('F:/python/1、Python快速入门（8天零基础入门到精通）/资料/第1-12章资料/课件/07-Python函数进阶.pptx', 'r', encoding='gbk', errors='replace') as f:
#     print(f"数据：\t{f.readlines()}")

# 关闭文件
f.close()

# 文件的写入 文件如果不存在，使用”w”模式，会创建新文件，文件如果存在，使用”w”模式，会将原有内容清空
f = open('data.txt', 'w')
f.write('丢你老母') # 此时会缓存在缓冲区，刷新内容以后才是真正写入到了文件中
# 刷新文件内容
f.flush()

# 文件的追加 文件不存在会创建文件
f = open('data.txt', 'a')
f.write('追加的内容Wn') # 此时会缓存在缓冲区，刷新内容以后才是真正写入到了文件中
# 刷新文件内容
f.flush()

# 文件操作案例
source_file = open('test.txt', 'r', encoding='UTF-8')
target_file = open('save.txt', 'w', encoding='UTF-8')
print(type(source_file))
for x in source_file:
    if x.count('正式'):
        target_file.write(x)
source_file.close()
target_file.close()

