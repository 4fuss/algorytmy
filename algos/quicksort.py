# -*- coding: utf-8 -*-


def partition(lst, prt, r):
    """returns the position of pivot"""
    pos = prt
    for i in range(prt, r):
        if lst[i] < lst[r]:
            lst[pos], lst[i] = lst[i], lst[pos]
            pos += 1

    lst[pos], lst[r] = lst[r], lst[pos]

    return pos


def qs_rec(lst, start, end):
    if start < end:
        pos = partition(lst, start, end)
        qs_rec(lst, start, pos - 1)
        qs_rec(lst, pos, end)


def quicksort(lst):
    return qs_rec(lst, 0, len(lst) - 1)


lst = [3, 45, 1, 2, 34]
quicksort(lst)
print(lst)




