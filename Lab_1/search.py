from math import floor
import math


def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1


def binary_search(values, item, low, high):
    mid = math.floor((low + high)/2)

    if low > high:
        return -1

    elif item < values[mid]:
        return binary_search(values, item, low, mid)
    elif item > values[mid]:
        return binary_search(values, item, mid+1,  high)
    else:
        return mid

# print(binary_search([1, 1, 3, 4, 7, 9], 7, 0, 5))
