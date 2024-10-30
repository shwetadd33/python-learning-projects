"""
Map: Map means dividing the work between multiple units i.e. cores in case of CPU

Reduce: Means aggregating all results from different cores, back to a one common or single output

"""

from multiprocessing import Pool
import time

def f(n):
    sum = 0
    for x in range(1000):
        sum += x*x
    return sum


if __name__ == "__main__":
    t1 = time.time()
    p = Pool()
    result = p.map(f, range(100000))
    p.close()
    p.join()    # It makes sure all the units/cores done executing their work

    print("Pool took: ", time.time() - t1)

    t2 = time.time()
    result = []
    for x in range(100000):
        result.append(f(x))

    print("Serial processing took: ", time.time() - t2)