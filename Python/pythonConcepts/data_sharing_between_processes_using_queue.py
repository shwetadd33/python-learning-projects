import multiprocessing

result = []


def cal_square(numbers, q):
    for n in numbers:
        q.put(n * n)


if __name__ == "__main__":
    num = [10, 20, 30]
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=cal_square, args=(num, q))

    p.start()

    p.join()

    while q.empty() is False:
        print(q.get())
