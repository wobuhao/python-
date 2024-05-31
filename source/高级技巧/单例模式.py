from 单例模式_class import str_tool


class StrTools:
    pass


s1 = StrTools()
s2 = StrTools()
print(s1)
print(s2)
print(id(s1))
print(id(s2))

s3 = str_tool
s4 = str_tool
print(s3)
print(s4)
