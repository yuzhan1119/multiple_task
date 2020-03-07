import threading
import time


def sing():
    """
    此為t1 threading的目標執行函數，當此還數完成後，threading結束
    :return:
    """
    for i in range(10):
        print(f'------- singing {i}-------')
        print('當前threading', threading.current_thread())
        time.sleep(1)


def dance():
    """
    此為t2 threading的目標執行函數，當此還數完成後，threading結束
    :return:
    """
    for j in range(5):
        print(f'------- dancing {j}-------')
        print('當前threading', threading.current_thread())
        time.sleep(1)


def main():
    """
    當main threading結束，程序結束
    :return:
    """
    print('## main threading ##', threading.enumerate())
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    print('## main threading ## --> t1 threading 開始: ', threading.enumerate())
    t2.start()
    print('## main threading ## --> t2 threading 開始: ', threading.enumerate())
    while True:
        print('所有 threading: ', threading.enumerate())
        if len(threading.enumerate()) <= 1:
            break
        time.sleep(1)


if __name__ == '__main__':
    main()
