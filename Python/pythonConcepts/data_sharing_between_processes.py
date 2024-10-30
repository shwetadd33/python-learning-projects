import multiprocessing

result = []


def cal_square(numbers, result, val):
    val.value = 5.45
    for idx, n in enumerate(numbers):
        result[idx] = n * n
    print("inside process result: ", result[:])


if __name__ == "__main__":
    num = [10, 20, 30]
    result = multiprocessing.Array('i', 3)
    val = multiprocessing.Value('d', 0.0)
    p = multiprocessing.Process(target=cal_square, args=(num, result,val))

    p.start()

    p.join()

    print("Outside process result: ", result[:])
    print("Value is:", val.value)