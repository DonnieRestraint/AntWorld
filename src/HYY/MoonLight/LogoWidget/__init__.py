import threading
import time
from queue import Queue

def put_id():
    i = 0
    while True:
        i = i + 1
        print("添加数据", i, id_queue.qsize())
        time.sleep(0.1)
        id_queue.put(i)

def get_id(m):
    while True:
        print(id_queue.full())
        i = id_queue.get()
        print("线程", m, '取值', i, id_queue.qsize())
        time.sleep(0.12)


if __name__ == "__main__":


    id_queue = Queue(3)

    Th1 = threading.Thread(target=put_id, )

    Th2 = threading.Thread(target=get_id, args=(2, ))
    # Th3 = threading.Thread(target=get_id, args=(3, ))
    # Th5 = threading.Thread(target=get_id, args=(4, ))
    # Th4 = threading.Thread(target=get_id, args=(5, ))

    Th1.start()

    Th2.start()
    # Th3.start()
    # Th4.start()
    # Th5.start()
