import unittest
from lab3 import BinaryTree, binary_tree_diameter


class TestBinaryTreeDiameter(unittest.TestCase):

    def test_example_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(3)
        root.right = BinaryTree(2)

        root.left.left = BinaryTree(7)
        root.left.right = BinaryTree(4)

        root.left.left.left = BinaryTree(8)
        root.left.left.left.left = BinaryTree(9)

        root.left.right.right = BinaryTree(5)
        root.left.right.right.right = BinaryTree(6)

        self.assertEqual(binary_tree_diameter(root), 6)

    def test_single_node(self):
        root = BinaryTree(1)
        self.assertEqual(binary_tree_diameter(root), 0)

    def test_empty_tree(self):
        self.assertEqual(binary_tree_diameter(None), 0)


if __name__ == "__main__":
    unittest.main()
