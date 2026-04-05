import unittest
from lab5 import count_islands_with_visualization


class TestIslands(unittest.TestCase):

    def test_example(self):
        grid = [
            [1, 0, 1],
            [0, 0, 1],
            [1, 0, 0]
        ]
        self.assertEqual(count_islands_with_visualization(grid), 3)

    def test_empty(self):
        self.assertEqual(count_islands_with_visualization([]), 0)

    def test_one_island(self):
        grid = [
            [1, 1],
            [1, 1]
        ]
        self.assertEqual(count_islands_with_visualization(grid), 1)

    def test_no_islands(self):
        grid = [
            [0, 0],
            [0, 0]
        ]
        self.assertEqual(count_islands_with_visualization(grid), 0)


if __name__ == "__main__":
    unittest.main()
