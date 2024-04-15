"""
This program has unit testing for stat computation from another program
"""
from computeStat import calculate_stat
import unittest

class TestStatistics(unittest.TestCase):

    def test_mean(self):
        data = [1, 2, 3, 4, 5]
        result = calculate_stat(data)
        self.assertEqual(result["mean"], 3.0)

    def test_median(self):
        data = [1, 2, 3, 4, 5]
        result = calculate_stat(data)
        self.assertEqual(result["median"], 3)

    def test_std(self):
        data = [1, 2, 3, 4, 5]
        result = calculate_stat(data)
        self.assertAlmostEqual(result["std"], 1.414213562373095, places=4)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            calculate_stat([])

    def test_single_element(self):
        data = [5]
        result = calculate_stat(data)
        self.assertEqual(result["mean"], 5)
        self.assertEqual(result["median"], 5)
        self.assertEqual(result["std"], 0)

if __name__=='__main__':
    unittest.main()