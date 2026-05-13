import unittest
import os
from lab7 import calculate_max_flow


class TestMaxFlow(unittest.TestCase):

    def test_small_graph(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(BASE_DIR, "roads.csv")

        result = calculate_max_flow(file_path)
        self.assertTrue(result >= 0)


if __name__ == "__main__":
    unittest.main()
