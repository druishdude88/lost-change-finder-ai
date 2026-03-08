# Test Program for Lost Change Finder AI

import unittest
from lost_change_finder import find_change  # Assuming the main program file is named lost_change_finder.py

class TestLostChangeFinder(unittest.TestCase):

    def test_example_case_1(self):
        self.assertEqual(find_change([0.25, 0.5, 0.75], 1.0), [0.25, 0.75])

    def test_example_case_2(self):
        self.assertEqual(find_change([0.1, 0.2, 0.3], 0.5), [0.2, 0.3])

    def test_no_combination(self):
        self.assertEqual(find_change([0.1, 0.2, 0.3], 0.7), None)

    def test_single_element(self):
        self.assertEqual(find_change([0.5], 0.5), [0.5])

if __name__ == '__main__':
    unittest.main()