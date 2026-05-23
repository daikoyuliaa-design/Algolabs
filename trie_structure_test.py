import unittest
from trie_structure import Trie, build_trie_from_patterns, TrieNode

class TestTrieStructure(unittest.TestCase):

    def setUp(self):
        """Метод виконується перед кожним тестом. Створюємо свіже дерево."""
        self.trie = Trie()

    def test_insert_and_search_exact_match(self):
        """Тест: слово успішно вставляється і знаходиться."""
        self.trie.insert("apple")
        self.assertTrue(self.trie.search("apple"))

    def test_search_non_existent_word(self):
        """Тест: пошук слова, якого взагалі немає в дереві."""
        self.trie.insert("apple")
        self.assertFalse(self.trie.search("banana"))

    def test_search_partial_word_is_not_full_word(self):
        """Тест: пошук частини слова (префіксу) як повноцінного слова."""
        self.trie.insert("apple")
        self.assertFalse(self.trie.search("app"))

    def test_starts_with_valid_prefix(self):
        """Тест: пошук коректного префіксу."""
        self.trie.insert("apple")
        self.assertTrue(self.trie.starts_with("app"))
        self.assertTrue(self.trie.starts_with("apple"))

    def test_starts_with_invalid_prefix(self):
        """Тест: пошук префіксу, якого немає."""
        self.trie.insert("apple")
        self.assertFalse(self.trie.starts_with("b"))
        self.assertFalse(self.trie.starts_with("applce"))

    def test_build_trie_from_patterns_function(self):
        """Тест: перевірка окремої функції побудови дерева зі списку."""
        patterns = ["cat", "car", "dog", "cart"]
        trie_from_func = build_trie_from_patterns(patterns)

        for word in patterns:
            self.assertTrue(trie_from_func.search(word))

        self.assertTrue(trie_from_func.starts_with("ca"))
        self.assertTrue(trie_from_func.starts_with("do"))

        self.assertFalse(trie_from_func.search("duck"))

    def test_property_validation(self):
        """Тест: перевірка, що сетер захищає від неправильного типу даних."""
        node = TrieNode()
        with self.assertRaises(TypeError):
            node.is_end_of_word = "Not A Boolean"


if __name__ == "__main__":
    unittest.main()
