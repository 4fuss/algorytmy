# -*- coding: utf-8 -*-


def mergesort(list):
    len_list = len(list)
    if len_list < 2:
        return list
    middle = len_list / 2
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])
    return merge(left, right)


def merge(list_a, list_b):
    result = []
    i, j = 0, 0
    while len(list_a) > i and len(list_b) > j:
        if list_a[i] <= list_b[j]:
            result.append(list_a[i])
            i += 1
        else:
            result.append(list_b[j])
            j += 1
    result += list_a[i:]
    result += list_b[j:]
    return result

unsorted = [6, 4, 7, 5, 2, 1]
res = mergesort(unsorted)
print res
