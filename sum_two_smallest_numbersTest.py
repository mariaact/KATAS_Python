import unittest
from sum_two_smallest_numbers import sum_two_smallest_numbers

class TestMiPrograma(unittest.TestCase):
    def test1(self):
        self.assertEqual(sum_two_smallest_numbers([5, 8, 12, 18, 22]), 13)
    def test2(self):
        self.assertEqual(sum_two_smallest_numbers([7, 15, 12, 18, 22]), 19)

    def test3(self):
        self.assertEqual(sum_two_smallest_numbers([25, 42, 12, 18, 22]), 30)

    def test4(self):
        self.assertEqual(sum_two_smallest_numbers([1,2,80,90,85,45]), 3)

    def test5(self):
         self.assertEqual(sum_two_smallest_numbers([1,1,80,5,42,10]), 2)
         

        