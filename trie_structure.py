class TrieNode: 
    def __init__(self):
        self._children = {}
        self._is_end_of_word = False

    @property
    def children(self) -> dict:
        """Гетер для отримання словника дочірніх вузлів."""
        return self._children

    @property
    def is_end_of_word(self) -> bool:
        """Гетер для перевірки, чи є вузол кінцем слова."""
        return self._is_end_of_word

    @is_end_of_word.setter
    def is_end_of_word(self, value: bool) -> None:
        """Сетер для зміни прапорця кінця слова."""
        if not isinstance(value, bool):
            raise TypeError("Прапорець має бути булевого типу (True/False)!")
        self._is_end_of_word = value


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None: 
        current = self.root 
        for char in word: 
            if char not in current.children: 
                current.children[char] = TrieNode()
            current = current.children[char] 

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word  

    def starts_with(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True


def build_trie_from_patterns(patterns: list[str]) -> Trie:
    trie = Trie()
    for pattern in patterns:
        trie.insert(pattern)
    return trie
