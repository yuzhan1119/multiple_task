"""
在一個函數中，對全局變量進行修改時，
到底需要使用global，要看對全局變量的指向
進行修改，如果修改了指向，讓全局變量指向了一個新的地方
則需要使用global，
如果只是修改了全局變量指向的空間中的數據，
則不需要使用global
"""

# 定義一個全局變量
import threading
import time

g_num = 100


def test1():
    global g_num
    g_num += 1
    print(f'test1 g_num value is {g_num}')


def test2():
    print(f'test2 g_num value is {g_num}')


def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)

    t1.start()
    time.sleep(1)

    t2.start()


if __name__ == '__main__':
    main()
