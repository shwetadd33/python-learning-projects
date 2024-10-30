"""
Multithreading : To handle multiple tasks at once

multithreading is used when CPU is idle , During that time if we want to optimize the performance of a program and
wants CPU to do some task



Note About Daemon threads : Some threads do background tasks, like sending keepalive packets,
or performing periodic garbage collection, or whatever. These are only useful when the main program is running,
and it's okay to kill them off once the other, non-daemon, threads have exited.
Without daemon threads, you'd have to keep track of them, and tell them to exit, before your program can completely quit.
By setting them as daemon threads, you can let them run and forget about them, and when your program quits,
any daemon threads are killed automatically.

There is one of the best examples of a daemon thread is Garbage Collector

SYNTAX:
# Set the thread as a daemon thread
thread.daemon = True

"""
import time
import threading

def cal_square(numbers):
    print("calculate square of numbers")
    for n in numbers:
        time.sleep(0.2)
        print("Square : ", n*n)


def cal_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print("Cube : ", n*n*n)

arr = [2,3,5,8,7]

t = time.time()

t1 = threading.Thread(target=cal_square,args=(arr,))
t2 = threading.Thread(target=cal_cube,args=(arr,))

t1.start()            # start() function will start executing threads
t2.start()

t1.join()              # .join() function will block the execution of the main thread until the given thread is not executed completely.
t2.join()


#cal_square(arr)
#cal_cube(arr)

print("Done in :", time.time()-t)
