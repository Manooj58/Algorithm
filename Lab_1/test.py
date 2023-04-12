import unittest
from search import linear_search, binary_search


class SearchTestCase(unittest.TestCase):
    def test_linear_search(self):
        values = [5, 3, 6, 1, 4, 9, 0]
        self.assertEqual(linear_search(values, 5), 0)
        self.assertEqual(linear_search(values, 1), 3)

    # def test_binary_search(self):
    # 	values = [1,2,3,4,5,6]
    # 	self.assertEqual(binary_search(values, 3, 0, len(values)-1),  2)
    # 	self.assertEqual(binary_search(values, 5, 0, len(values)-1),  4)


if __name__ == '__main__':
    unittest.main()
