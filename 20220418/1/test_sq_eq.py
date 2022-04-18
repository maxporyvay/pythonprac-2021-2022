import unittest
from prog import solveSquare

class TestSqEq(unittest.TestCase):

    def test_positive_d(self):
        self.assertEqual(solveSquare(1, -3, 2), (1, 2))

    def test_negative_d(self):
        self.assertEqual(solveSquare(1, 1, 1), None)
        
    def test_zero_d(self):
        self.assertEqual(solveSquare(1, -2, 1), (1, 1))
        
    def test_zero_d_(self):
        self.assertEqual(solveSquare(2, 3, 1.125), (-0.75, -0.75))

    def test_positive_d_(self):
        self.assertEqual(solveSquare(2, 3, 1), (-1, -0.5))
