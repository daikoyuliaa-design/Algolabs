import unittest
import os
import sys
from io import StringIO
from LABA2 import aggressive_cows, read_from_file

class TestCows(unittest.TestCase):
    def setUp(self):
        self.filename = "temp_input.txt"
        with open(self.filename, "w") as f:
            f.write("5 3\n1 2 8 4 9")
        self.held, sys.stdout = sys.stdout, StringIO()

    def tearDown(self):
        sys.stdout = self.held
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_logic_from_example(self):
        self.assertEqual(aggressive_cows([1, 2, 8, 4, 9], 3), 3)

    def test_file_reading(self):
        n, c, stalls = read_from_file(self.filename)
        self.assertEqual(aggressive_cows(stalls, c), 3)

    def test_two_cows_only(self):
        self.assertEqual(aggressive_cows([1, 10, 100], 2), 99)

if __name__ == "__main__":
    filename = "input.txt"
    with open(filename, "w") as f:
        f.write("5 3\n1 2 8 4 9")
    os.startfile(filename)

    sections_val = [1, 2, 8, 4, 9]
    print(f"Максимальна мінімальна відстань: {aggressive_cows(sections_val, 3)}")

    unittest.main()
