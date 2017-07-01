import random

import math

from tools.timer3 import bestof


def merge_sort(list):
    if len(list) < 2:
        return list

    # // will make half an Int
    mid = len(list) // 2
    result = []
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])

    while (len(left) > 0) and (len(right) > 0):
        if (left[0] > right[0]):
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))
    # print(result)
    result.extend(left + right)
    return result


def insertion_sort(list):
    for index in range(1, len(list)):
        j = index
        while (j > 0) and list[j] < list[j - 1]:
            list[j], list[j - 1] = list[j - 1], list[j]
            j -= 1
    return list


def select_sort(list):
    for index in range(len(list) - 1):
        smallest = index
        for comparision in range(len(list) - index - 1):
            if list[smallest] > comparision:
                smallest = comparision
        list[index], list[comparision] = list[comparision], list[index]
    return list


def bubble_sort(list):
    unordered = True
    while unordered is True:
        unordered = False
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                unordered = True
    return  list

# test_list = (random.sample(range(100), 50))
test_list = [7, 84, 89, 47, 73, 24, 91, 55, 70, 44, 23, 80, 3, 25, 94, 58, 64, 17, 76, 12, 6, 87, 42, 51, 75, 20, 30,
             22, 74, 41, 61, 52, 53, 1, 27, 56, 38, 79, 83, 93, 4, 86, 90, 69, 0, 96, 46, 40, 67, 50]
print(test_list)
time = bestof(merge_sort, test_list)
time2 = bestof(insertion_sort, test_list)
time3 = bestof(select_sort, test_list)
time4 = bestof(bubble_sort,test_list)
print(time[0])
print(time2[0])
print(time3[0])
print(time4[0])
# merge_sort(test_list)
