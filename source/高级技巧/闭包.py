def outer(logo):
    def inner(msg):
        print(f"<{logo}>{msg}<{logo}>")

    return inner


fn1 = outer("马里奥")
fn1("哈哈")


# 使用nonlocal关键字修改外部函数的值


def outer2(num1):
    def inner2(num2):
        nonlocal num1
        num1 += num2
        print(num1)

    return inner2


fn2 = outer2(10)

fn2(10)


def account_create(count=0):
    def inner(num, deposit=True):
        nonlocal count
        if deposit:
            count += num
            print(f"存款：+{num}, 账户余额：{count}")
        else:
            count -= num
            print(f"取款：-{num}, 账户余额：{count}")

    return inner


atm = account_create()
atm(100)
atm(15)
atm(102, deposit=False)
