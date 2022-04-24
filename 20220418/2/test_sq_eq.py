import unittest
from unittest.mock import MagicMock, patch
from prog import solve, SquareIO

class TestSqEq(unittest.TestCase):

    def test_positive_d(self):
        SquareIO.inputCoeff = MagicMock(side_effect = [1, -3, 2])
        SquareIO.printResult = MagicMock()
        solve()
        result = SquareIO.printResult.call_args.args[0]
        assert result == (1, 2)

    def test_negative_d(self):
        SquareIO.inputCoeff = MagicMock(side_effect = [1, 1, 1])
        SquareIO.printResult = MagicMock()
        solve()
        result = SquareIO.printResult.call_args.args[0]
        assert result == None
        
    def test_zero_d(self):
        SquareIO.inputCoeff = MagicMock(side_effect = [1, -2, 1])
        SquareIO.printResult = MagicMock()
        solve()
        result = SquareIO.printResult.call_args.args[0]
        assert result == (1, 1)
        
    def test_zero_abc(self):
        SquareIO.inputCoeff = MagicMock(side_effect = [0, 0, 0])
        SquareIO.printResult = MagicMock()
        solve()
        result = SquareIO.printResult.call_args.args[0]
        assert result == '(-inf, +inf)'
        
    def test_zero_ab(self):
        SquareIO.inputCoeff = MagicMock(side_effect = [0, 0, 1])
        SquareIO.printResult = MagicMock()
        solve()
        result = SquareIO.printResult.call_args.args[0]
        assert result == None
        
    def test_zero_a(self):
        SquareIO.inputCoeff = MagicMock(side_effect = [0, -2, 1])
        SquareIO.printResult = MagicMock()
        solve()
        result = SquareIO.printResult.call_args.args[0]
        assert result == (0.5, 0.5)
        
    def test_incorrect_input(self):
        SquareIO.inputCoeff = MagicMock(side_effect = [0, -2, 'hello'])
        SquareIO.printResult = MagicMock()
        with self.assertRaises(ValueError):
            solve()
