import re

s = "hy aa"
# match 从头匹配
result = re.match("hy", s)
# print(result)
# print(result.span())
# print(result.group())

# search 搜索整个字符串，找出匹配的，只会找出第一个匹配的
result = re.search('a', s)
# print(result)
# print(result.span())
# print(result.group())

# findall 匹配整个字符串，找出全部匹配项
s = 'hyhyaahyhyhahahahah'
result = re.findall('ha', s)
# print(result)

"""
元字符匹配
.   匹配任意1个字符（除了\n），\. 匹配点本身
[]  匹配[]中列举的字符
\d  匹配数字，即0-9
\D  匹配非数字
\s  匹配空白，即空格、tab键
\S  匹配非空白
\w  匹配单词字符，即a-z、A-Z、0-9、-
\W  匹配非单词字符
"""

"""
数量匹配
*       匹配前一个规则的字符出现0至无数次
+       匹配前一个规则的字符出现1至无数次
?       匹配前一个规则的字符出现0次或1次
{m}     匹配前一个规则的字符出现m次
{m,}    匹配前一个规则的字符出现最少m次
{m,n}   匹配前一个规则的字符出现m到n次
"""

"""
边界匹配
^       匹配字符串开头
$       匹配字符串结尾
\b      匹配一个单词的边界
\B      匹配非单词边界
"""

"""
分组匹配
|       匹配左右任意一个表达式
()      将括号中字符作为一个分组
"""

s = "haha嘿嘿123~！@#￥%……&*（）——+  《》、|"
result = re.findall(r'\W', s)
# print(result)


# 匹配账号，只能由字母和数字组成，长度限制6-10位
r = '^[0-9a-zA-Z]{6,10}$'
s = '1234567'
print(re.findall(r, s))

# 匹配QQ号，要求纯数字，长度5-11，第一位不为0
r = '^[1-9][0-9]{4,10}$'
s = '01234567'
print(re.findall(r, s))

# 匹配邮箱地址，只允许qq、163、gmail这三种邮箱地址
r = '^[.][/'']$'
s = '1234567'
print(re.findall(r, s))
