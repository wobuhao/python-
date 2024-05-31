import time
import threading

"""
多线程
thread_obj = threading.Thread([group, [, target [, name [, args [, kwargs]]]]])
- group: 暂时无用，未来功能的预留参数
- target: 执行的目标任务名
- args: 以元祖的方式给执行任务传参
- kwargs: 以字典方式给执行任务传参
- name: 线程名，一般不用设置
"""


def sing(msg):
    while True:
        print(msg)
        time.sleep(1)


def dance(msg):
    while True:
        print(msg)
        time.sleep(1)


if __name__ == '__main__':
    # 定义一个线程
    sing_thread = threading.Thread(target=sing, args=('在唱歌哦~',))
    dance_thread = threading.Thread(target=dance, kwargs={"msg": '在跳舞哦~'})
    # 执行线程
    sing_thread.start()
    dance_thread.start()
