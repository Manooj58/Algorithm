from random import sample
from search import linear_search
from search import binary_search
from time import time_ns


def run(n):
    data = sample(range(1, n+1), n)
    # for Binary search
    # data = range(1, n+1)

    start_time = time_ns()
    linear_search(data, data[-1])
    # binary_search(data, data[-1], 0, len(data))
    end_time = time_ns()
    time_taken = end_time-start_time
    print(time_taken)


for i in range(1, 7):
    n = 1000000*i
    run(n)
