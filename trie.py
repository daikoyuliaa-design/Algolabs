import heapq
import sys
from pathlib import Path


class TrieNode:
    def __init__(self):
        self._children = {}
        self._is_end_of_word = False
        self.frequency = 0

    @property
    def children(self) -> dict:
        return self._children

    @property
    def is_end_of_word(self) -> bool:
        return self._is_end_of_word

    @is_end_of_word.setter
    def is_end_of_word(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise TypeError("Прапорець має бути булевого типу (True/False)!")
        self._is_end_of_word = value


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, frequency: int = 1) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True
        current.frequency = frequency

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

    def _find_node(self, prefix: str) -> "TrieNode | None":
        """Повертає вузол на кінці префіксу або None."""
        current = self.root
        for char in prefix:
            if char not in current.children:
                return None
            current = current.children[char]
        return current

    def _collect_words(self, node: TrieNode, prefix: str,
                       results: list) -> None:
        """DFS — збирає всі (частота, слово) з піддерева вузла."""
        if node.is_end_of_word:
            results.append((node.frequency, prefix))
        for char, child in node.children.items():
            self._collect_words(child, prefix + char, results)

    def top_n_completions(self, prefix: str, n: int = 3) -> list[str]:
        """
        Повертає до n найпоширеніших слів, що починаються з prefix.
        Якщо prefix - порожній рядок, шукає серед усіх слів.
        """
        node = self._find_node(prefix)
        if node is None:
            return []

        candidates: list[tuple[int, str]] = []
        self._collect_words(node, prefix, candidates)

        top = heapq.nlargest(n, candidates, key=lambda x: x[0])
        return [word for _, word in top]


def build_trie_from_patterns(patterns: list[str]) -> Trie:
    trie = Trie()
    for pattern in patterns:
        trie.insert(pattern)
    return trie


def load_words_from_file(filepath: str | Path) -> list[tuple[str, int]]:
    words: list[tuple[str, int]] = []
    path = Path(filepath)

    if not path.exists():
        raise FileNotFoundError(f"Файл зі словами не знайдено: {path}")

    with path.open(encoding="utf-8") as fh:
        for lineno, raw_line in enumerate(fh, start=1):
            line = raw_line.strip()

            if not line or line.startswith("#"):
                continue

            parts = line.split()
            if len(parts) != 2:
                raise ValueError(
                    f"{path}:{lineno}: очікується «слово частота», "
                    f"отримано: {line!r}"
                )

            word, freq_str = parts
            if not freq_str.isdigit():
                raise ValueError(
                    f"{path}:{lineno}: частота має бути цілим числом, "
                    f"отримано: {freq_str!r}"
                )

            words.append((word.lower(), int(freq_str)))

    return words


def build_trie_with_frequency(word_freq: list[tuple[str, int]]) -> Trie:
    trie = Trie()
    for word, freq in word_freq:
        trie.insert(word, freq)
    return trie


DEFAULT_WORDS_FILE = "words.txt"


def main() -> None:

    words_file = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_WORDS_FILE

    try:
        word_freq = load_words_from_file(words_file)
    except (FileNotFoundError, ValueError) as exc:
        print(f"Помилка: {exc}")
        sys.exit(1)

    trie = build_trie_with_frequency(word_freq)
    total = len(word_freq)
    print(f"Завантажено {total} українських слів із «{words_file}».")
    print("Введіть слово або префікс для автодоповнення (або 'вихід' для виходу).\n")

    while True:
        user_input = input("Префікс: ").strip().lower()

        if user_input in ("вихід", "exit", "quit"):
            print("До побачення!")
            break

        if not user_input:
            print("  (порожній рядок — спробуйте ще раз)\n")
            continue

        suggestions = trie.top_n_completions(user_input, n=3)

        if suggestions:
            print(f"  Топ-3 найпоширеніших слова з «{user_input}»:")
            for i, word in enumerate(suggestions, 1):
                print(f"    {i}. {word}")
        else:
            print(f"  Слів з префіксом «{user_input}» не знайдено.")
        print()


if __name__ == "__main__":
    main()
