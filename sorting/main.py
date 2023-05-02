from random import sample
from insertion import insertion_sort
from merge_sort import merge_sort
from time import time


def run(n):
    data = sample(range(1, n+1), n)
    start_time = time()
    # insertion_sort(data)
    merge_sort(data, 0, len(data)-1)
    end_time = time()
    time_taken = end_time - start_time
    print(f"{n} data = {time_taken}")
    # print(time_taken)


if __name__ == "__main__":
    n = 10000
    for i in range(10):
        run(n*i)
