"""
Lock: Whenever the 2 threads/processes try to access the shared resource such as shared memory, files or database it can
create a problem. So we need Lock to avoid this.
"""

import time
import multiprocessing


def deposit(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()


def withdraw(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()


if __name__ == "__main__":
    balance = multiprocessing.Value('i', 200)
    lock = multiprocessing.Lock()
    d = multiprocessing.Process(target=deposit, args=(balance, lock))
    w = multiprocessing.Process(target=withdraw, args=(balance, lock))

    d.start()
    w.start()

    d.join()
    w.join()

    print("Balance is: ", balance.value)
