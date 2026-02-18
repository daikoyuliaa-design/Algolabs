import unittest
from laba1 import find_longest_peak_sequence


class TestPeakSequence(unittest.TestCase):


    def test_example(self):
        """Тест на масиві із прикладу в завданні"""
        arr = [1, 3, 5, 4, 2, 8, 3, 7]
        self.assertEqual(find_longest_peak_sequence(arr), 5)

    def test_sorted_ascending(self):
        """Тест на зростаючому масиві"""
        arr = [1, 2, 3, 4, 5, 6]
        self.assertEqual(find_longest_peak_sequence(arr), 0)

    def test_sorted_descending(self):
        """Тест на спадному масиві"""
        arr = [6, 5, 4, 3, 2, 1]
        self.assertEqual(find_longest_peak_sequence(arr), 0)

    def test_two_elements(self):
        """Тест на масиві з двох елементів"""
        arr = [1, 2]
        self.assertEqual(find_longest_peak_sequence(arr), 0)

    def test_no_peaks(self):
        """Тест на масиві без піків"""
        arr = [1, 2, 2, 2, 1]
        self.assertEqual(find_longest_peak_sequence(arr), 0)

    def test_multiple_peaks(self):
        """Тест на масиві з трьома піками"""
        arr = [1, 3, 2, 4, 3, 2, 5, 1]
        self.assertEqual(find_longest_peak_sequence(arr), 4)


if __name__ == "__main__":
    unittest.main()
