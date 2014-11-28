# -*- coding: utf-8 -*-
import unittest
from ..algos.mergesort import *
from ..algos.inversions import *


class Is_Sorted(unittest.TestCase):

    def sort_even_list_no_doubles_test(self):
        self.unsorted = [6, 4, 7, 5, 2, 1]
        self.sorted_arr = [1, 2, 4, 5, 6, 7]
        ms_result = mergesort(self.unsorted)
        self.assertEqual(ms_result, self.sorted_arr)

    def count_inversions_test(self):
        arr = [1, 3, 5, 2, 4, 6]
        ans = 3
        self.assertEqual(inversions(arr), ans)

        arr = [1, 5, 3, 2, 4]
        ans = 4
        self.assertEqual(inversions(arr), ans)

        arr = [5, 4, 3, 2, 1]
        ans = 10
        self.assertEqual(inversions(arr), ans)

        arr = [1, 6, 3, 2, 4, 5]
        ans = 5
        self.assertEqual(inversions(arr), ans)


if __name__ == '__main__':
    unittest.main()