# import math
# from sys import maxsize


# def merge_sort(array, start, end):
#     if start < end:
#         mid = math.floor((start+end)/2)
#         merge_sort(array, start, mid)
#         merge_sort(array, mid+1, end)
#         merge(array, start, mid, end)
#     return array


# def merge(array, start, mid, end):
#     n1 = mid - start + 1
#     n2 = end - mid
#     L = [0]*(n1+1)
#     R = [0]*(n2+1)

#     for i in range(n1):
#         L[i] = array[start+i]
#     for j in range(n2):
#         R[j] = array[mid+j+1]

#     L[n1] = maxsize
#     R[n2] = maxsize

#     i = 0
#     j = 0

#     for k in range(start, end+1):
#         if L[i] <= R[j]:
#             array[k] = L[i]
#             i = i+1
#         else:
#             array[k] = R[j]
#             j = j+1
import math
from sys import maxsize


def merge_sort(array, start, end):
    if start < end:
        mid = math.floor((start+end)/2)
        merge_sort(array, start, mid)
        merge_sort(array, mid+1, end)
        merge(array, start, mid, end)
    return array


def merge(array, start, mid, end):
    n1 = mid - start + 1
    n2 = end - mid
    L = [0]*(n1+1)
    R = [0]*(n2+1)

    for i in range(n1):
        L[i] = array[start+i]
    for j in range(n2):
        R[j] = array[mid+j+1]

    L[n1] = maxsize
    R[n2] = maxsize

    i = 0
    j = 0

    for k in range(start, end+1):
        if L[i] <= R[j]:
            array[k] = L[i]
            i = i+1
        else:
            array[k] = R[j]
            j = j+1
