def test(a, b):
    print(a + b)

# 只有当程序是直接执行的才会进入if内部，如果是被导入的，则if无法进入
if __name__ == '__main__':
    test(1, 2)

