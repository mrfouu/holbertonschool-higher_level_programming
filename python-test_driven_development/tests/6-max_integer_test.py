#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        # find the max integer
        self.assertAlmostEqual(max_integer([1, 2, 6]), 6)
        self.assertAlmostEqual(max_integer([5, 2, 3, 0]), 5)
        self.assertAlmostEqual(max_integer([-11, -9, -121, -1]), -1)
        self.assertAlmostEqual(max_integer([-11, 1, 8, -3, 5]), 8)
        self.assertAlmostEqual(max_integer([69]), 69)
        self.assertAlmostEqual(max_integer([]), None)