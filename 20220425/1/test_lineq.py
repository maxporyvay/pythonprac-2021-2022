import unittest
from lineq import solve

class TestSqEq(unittest.TestCase):

    def test_1(self):
        self.assertEqual(solve(0, 5), None)

    def test_2(self):
        self.assertEqual(solve(0, 0), None)
        
    def test_3(self):
        self.assertEqual(solve(1, 0), 0)
        
    def test_4(self):
        self.assertEqual(solve(1, 1), -1)
