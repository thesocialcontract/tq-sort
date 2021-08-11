import unittest
import random
from learnsort.sorter import sort

class TestSorts(unittest.TestCase):
    def test_sort_empty(self):
        unsorted = [] 
        sorted_list = sort(unsorted) 
        expected = [] 
        self.assertEqual( sorted_list, expected )

    def test_sort_small(self):
        unsorted = [25, 10, 15, 5, 0, 20]
        sorted_list = sort(unsorted)
        expected = [0, 5, 10, 15, 20, 25]
        self.assertEqual( sorted_list, expected )

    def test_sort_small_with_duplicates(self):
        unsorted = [25, 10, 25, 5, 0, 20]
        sorted_list = sort(unsorted)
        expected = [0, 5, 10, 20, 25, 25]
        self.assertEqual( sorted_list, expected )

    def test_sort_small_with_negatives(self):
        unsorted = [25, 10, -15, -5, 0, 20]
        sorted_list = sort(unsorted)
        expected = [-15, -5, 0, 10, 20, 25]
        self.assertEqual( sorted_list, expected )

    def test_sort_small_presorted(self):
        unsorted = [0, 5, 10, 15, 20, 25]
        sorted_list = sort(unsorted)
        expected = [0, 5, 10, 15, 20, 25]
        self.assertEqual( sorted_list, expected )

    def test_sort_small_reversed(self):
        unsorted = [25, 20, 15, 10, 5, 0] 
        sorted_list = sort(unsorted)
        expected = [0, 5, 10, 15, 20, 25]
        self.assertEqual( sorted_list, expected )

    def test_sort_med_random(self):
        unsorted = random.sample( range(1000000), 10000)
        sorted_list = sort(unsorted)
        expected = sorted( unsorted )
        self.assertEqual( sorted_list, expected )

    def test_sort_large_random(self):
        unsorted = random.sample( range(1000000000), 1000000)
        sorted_list = sort(unsorted)
        expected = sorted( unsorted )
        self.assertEqual( sorted_list, expected )
