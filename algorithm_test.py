import unittest
from algorithm import QuickSort

class AcronymTest(unittest.TestCase):
    def test_basic_inorder(self):
        self.assertEqual(QuickSort([1,2,3,4,5,6]).Sort(), [1,2,3,4,5,6])
    def test_basic_reverse(self):
        self.assertEqual(QuickSort([6,5,4,3,2,1]).Sort(), [1,2,3,4,5,6])
    def test_basic_disorder(self):
        self.assertEqual(QuickSort([6,3,2,5,4,1]).Sort(), [1,2,3,4,5,6])
    def test_basic_with_same(self):
        self.assertEqual(QuickSort([5,3,2,5,4,2]).Sort(), [2,2,3,4,5,5])

if __name__ == '__main__':
    unittest.main()