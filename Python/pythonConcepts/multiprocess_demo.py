import time
import multiprocessing


def cal_square(numbers):
    for n in numbers:
        time.sleep(5)
        print("Square: ", n * n)


def cal_cube(numbers):
    for n in numbers:
        time.sleep(5)
        print("Cube: ", n * n * n)


if __name__ == "__main__":
    arr = [2, 3, 4, 5]
    p1 = multiprocessing.Process(target=cal_square, args=(arr,))
    p2 = multiprocessing.Process(target=cal_cube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("done")

