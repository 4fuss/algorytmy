# -*- coding: utf-8 -*-


def inversions(list):
    return mergesort_inv(list, 0)[1]


def mergesort_inv(list, inv):
    len_list = len(list)
    if len_list < 2:
        return list, inv
    middle = len_list / 2
    left, inv_left = mergesort_inv(list[:middle], inv)
    right, inv_right = mergesort_inv(list[middle:], inv)
    inv += inv_left + inv_right
    return merge_inv(left, right, inv)


def merge_inv(left, right, inv):
    result = []
    i, j = 0, 0
    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            inv += len(left) - i
            j += 1
    result += left[i:]
    result += right[j:]

    return result, inv
