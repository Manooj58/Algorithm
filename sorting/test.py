import unittest
from insertion import insertion_sort
from merge_sort import merge_sort


class InsertionSortTest(unittest.TestCase):
    def test_insertion_sort(self):
        values = [9, 8, 7, 6, 5]
        expected_value = [5, 6, 7, 8, 9]
        self.assertEqual(expected_value, insertion_sort(values))

    def test_insertion_sort_2(self):
        values = [4, 5, 6, 7, 8]
        expected_value = [4, 5, 6, 7, 8]
        self.assertEqual(expected_value, insertion_sort(values))

    def test_merge_sort(self):
        values = [1, 2, 4, 3, 7, 8, 9]
        expected_value = [1, 2, 3, 4, 7, 8, 9]
        self.assertEqual(expected_value, merge_sort(values, 0, 6))


if __name__ == '__main__':
    unittest.main()
