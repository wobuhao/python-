# 装饰器一般写法（闭包）
def outer(fnc):
    def inner():
        print(f"我要睡觉了")
        fnc()
        print(f"我起床了")

    return inner


def sleep():
    import random
    import time
    print(f"睡眠中。。。")
    time.sleep(random.randint(1, 5))


fn1 = outer(sleep)
fn1()

# 装饰器的快捷写法（语法糖）


def outer2(fnc):
    def inner():
        print(f"我要睡觉了")
        fnc()
        print(f"我起床了")

    return inner


@outer2
def sleep2():
    import random
    import time
    print(f"睡眠中。。。")
    time.sleep(random.randint(1, 5))

sleep2()