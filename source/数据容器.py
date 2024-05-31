"""
数据容器
    list 列表 [1, 2, 3] 元素可以是任意类型数据
    tuple 元祖 (1, 2, 3) 元素可以是任意类型数据
    str 字符串 "abc"
    set 集合  {True, False, False, 1, 'haha'} 元素可以是任意类型数据
    dict 字典、映射 {"name": "jack"}
"""

"""
1.list 列表
    a.可遍历 支持for、while循环
    b.可重复
    c.可修改
    d.有序的
"""
# list 列表 索引下标从0开始
list = [1, 2.25, 'hy', False, True, True, ['内嵌']]
# list = []
# list = list()

print(list)
print(f"根据list索引取出元素 {list[0]}, {list[-3]}, {list[-1][0]}")

# list 查询 index()
print(list.index('hy'))

# list 插入 index()
list.insert(2, '插入的元素')
print(list)

# list 根据下标修改元素值
list[0] = 120
print(list)

# list 追加元素1 append() 末尾追加
list.append('默认追加元素')
print(list)

# list 追加元素2 extend() 末尾追加一个列表
list.extend([1, 2, 3, 4])
print(list)

# list 删除元素 del
del list[1]
print(list)

# list 删除元素 pop
list.pop(1)
print(list)

# list 删除元素 romove()
list.remove('hy')
print(list)

# list 统计元素的重复次数 count()
print(list.count(True))

# list 反转 reverse()
list.reverse()
print(f"反转 {list}")

# list 排序 sort()
# list.sort() # 正向排序
# list.sort(reverse=True)  # 反向排序
print(f"排序 {list}")

# list 切片
print(f"切片：{list[2:]}")
print(f"切片：{list[1:3]}")

# list 是否包含某个值
if 'hy' in list:
    print("包含了：hy")
else:
    print("不包含：hy")

# list 统计列表有多少元素 len()
print(len(list))

print('最后一个元素值：%s' % list[len(list)-1])

# list 清空元素 clear()
# list.clear()
# print(list)

# list 遍历 while
list_index = 0
while list_index < len(list):
    print(f"while循环：{list[list_index]}", end='==')
    list_index += 1
print()

# list 遍历 for in
for i in list:
    print(f"list循环：{i}", end=' ')

"""
2.tuple 元祖 不可修改的列表
    a.可遍历 支持for、while循环
    b.可重复
    c.不可修改
    d.有序的
"""

# tuple 元祖 定义
# 只有一个元素时，需要添加 ,
t1 = (120,)
t1 = tuple()
t1 = (1, 2, False, True, False, '张飞', ('嵌套元祖', False), [1, 2, False, True])

# tuple 元祖 index() count() len()
print(t1.index(False))
print(t1.count(True))
print(len(t1))

# tuple 元祖内的list内容可以进行修改、增加、删除、反转等,但是不可替换为其他list列表
t1[len(t1)-1][0] = '被修改了'
print(t1[len(t1)-1][0])

# t1[len(t1)-1] = [False]  报错 TypeError: 'tuple' object does not support item assignment

# tuple 遍历 与列表遍历一致
index = 0
while index < len(t1):
    print(f"{t1[index]}", end='')
    index += 1

print("\n===============")

for x in t1:
    print(x, end='')


"""
3.str 字符串
    a.可遍历 支持for、while循环
    b.可重复
    c.不可修改
    d.有序的
"""

# str 字符串定义 无法修改
str1 = 'public'
str2 = "9:46:21"

# str 字符串 通过下标访问
print(f"\n{str1[1]}")
print(f"{str1[-1]}")

# str 字符串 查找下标 index()
print(str1.index('b'))

# str 字符串 替换 replace()
new_str1 = str1.replace('c', 'cing')
print(new_str1)

# str 字符串 分割 split()
new_list = "你 好".split(" ")
print(new_list)

# str 字符串 去除前后空格 strip() 也可去除字符串 strip(字符串)
new_str1 = " 去除前后空格 "
print(f"去除前后空格：{new_str1.strip()}")

new_str1 = "空格12"
#print(f"去除字符串：{new_str1.strip("12")}")

# str 字符串 统计字符串中某字符串的出现次数 count()
new_str1 = "1112789"
#print(f"统计字符串中某字符串的出现次数：{new_str1.count("1")}")

# str 字符串 长度 len()
print(f"长度：{len(new_str1)}")

# str 字符串 遍历与列表一致
index = 0
while index < len(new_str1):
    print(f"{new_str1[index]}", end='')
    index += 1
print()
for x in new_str1:
    print(f"{x}", end='')
print()

"""
4.序列 & 切片
"""
# 列表、元祖、字符串都属于序列
# 切片：序列[起始下标:结束下标:步长]
new_list = [1, 2, 3]
print(f"取出列表中下标2以后得元素：{new_list[2::1]}")
print(f"依次取出所有元素：{new_list[:]}")


new_tuple = (1, 2, 3)
print(f"取出元祖中下标1以后得元素：{new_tuple[0::2]}")

new_str = '123'
print(f"取出字符串中下标2以后得元素：{new_str[2:]}")

# 序列 实现序列的倒序：[::-1]
new_str = "万过薪月，员序程马黑来，nohtyP学"
temp_list = new_str.split("，")
print(temp_list[1][::-1].strip("来"))

"""
5.set 集合 注意：集合不支持下标索引访问，因为是无序的
    a.可遍历
    b.不可重复
    c.可修改
    d.无序的
"""

# set 集合定义
new_set = {}
new_set = set()
# 会自动去重
new_set = {True, False, False, 120, 'hymn'}

print(new_set)

# set 集合 添加新元素 add()
new_set.add("张飞")
print(f"{new_set}")

# set 集合 移除元素 remove()
new_set.remove("张飞")
print(f"{new_set}")

# set 集合 随机取出元素 pop()
element = new_set.pop()
print(f"随机取出元素:{element}， {new_set}")

# set 集合 清空元素 clear()
new_set.clear()
print(f"{new_set}")

# set 集合 取出两个集合的差集 集合1.difference(集合2)， 取出集合1和集合2的差集（集合1有而集合2没有的）
set1 = {1, 2, 8}
set2 = {2, 8, 5}
set3 = set1.difference(set2)
print(f"{set3}")

# set 集合 消除两个集合的差集 集合1.difference_update(集合2)， 对比集合1和集合2，在集合1内，删除和集合2相同的元素
set1 = {1, 2, 8}
set2 = {2, 8, 5}
set1.difference_update(set2)
print(f"{set1}")

# set 集合 两个集合合并 集合1.union(集合2)， 将集合1和集合2合并成一个新的集合
set1 = {1, 2, 8}
set2 = {2, 8, 5}
set3 = set1.union(set2)
print(f"{set3}")

# set 集合 集合长度 len()
set1 = {1, 2, 8}
print(f"{len(set1)}")

# set 集合 遍历 由于是无序的，所以无法使用while进行遍历
set1 = {1, 2, 8}
for x in set1:
    print(f"{x}\t", end='')

"""
6.dict 字典 
    a.Key不可重复
    b.无序的
    c.可遍历key 只支持for循环
    c.可修改
"""

# dict 字典 定义
new_dict = dict()
new_dict = {}
new_dict = {"name": 'hy', "age": 18, "hobby": {'爱好1': '跳街舞', '爱好2': 'rap', '爱好3': '写代码'}}
print(f"\n{new_dict['hobby']['爱好1']}")

# dict 字典 新增、更新元素
new_dict['father'] = 'hh'
print(f"{new_dict}")
new_dict['hobby']['爱好2'] = "打篮球"
print(f"{new_dict}")

# dict 字典 删除元素 pop()
new_dict.pop("age")
print(f"{new_dict}")

# dict 字典 清空元素 clear()
# new_dict.clear()
# print(f"{new_dict}")

# dict 字典 获取全部的key keys()
print(f"{new_dict.keys()}")

# dict 字典 遍历key
for x in new_dict.keys():
    print(f"key:{x},value:{new_dict[x]}\t")

# dict 字典 获取长度 len()
print(f"{len(new_dict)}")

"""
序列总结
1.是否支持下标索引
  支持：列表、元组、字符串 - 序列类型
  不支持：集合、字典 - 非序列类型
  
2.是否支持重复元素：
  支持：列表、元组、字符串 - 序列类型
  不支持：集合、字典 - 非序列类型
  
3.是否可以修改
  支持：列表、集合、字典
  不支持：元组、字符串
  
4.5类数据容器都支持for循环遍历
  列表、元组、字符串支持while循环，集合、字典不支持（无法下标索引）
  
5.统计
  a.len(容器) 容器长度
  b.max(容器) 容器最大的元素
  c.min(容器) 容器最小的元素
  
6.容器互转
  a.list(容器) 将给定容器转换为列表
  b.str(容器) 将给定容器转换为字符串
  c.tuple(容器) 将给定容器转换为元组
  d.set(容器) 将给定容器转换为集合
   
7. 排序
  a.sorted(容器,[reverse=True]) 将给定容器进行排序,排序后都会得到列表list对象
  
list 列表 [1, 2, 3] 元素可以是任意类型数据
tuple 元祖 (1, 2, 3) 元素可以是任意类型数据
str 字符串 "abc" 
set 集合  {True, False, False, 1, 'haha'} 元素可以是任意类型数据
dict 字典、映射 {"name": "jack"}
  
"""