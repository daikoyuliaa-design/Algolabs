import sys

def find_max_chain(words):
    if not words:
        return 0

    max_len = 0
    for w in words:
        if len(w) > max_len:
            max_len = len(w)

    buckets = [[] for _ in range(max_len + 1)]
    for w in words:
        buckets[len(w)].append(w)

    word_chains = {}
    max_overall_chain = 0

    for length in range(1, max_len + 1):
        for word in buckets[length]:
            current_max = 1
            for i in range(length):
                shorter_word = word[:i] + word[i+1:]
                if shorter_word in word_chains:
                    potential_chain = word_chains[shorter_word] + 1
                    if potential_chain > current_max:
                        current_max = potential_chain

            word_chains[word] = current_max
            if current_max > max_overall_chain:
                max_overall_chain = current_max

    return max_overall_chain

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    if input_data[0].isdigit():
        words = input_data[1:]
    else:
        words = input_data

    result = find_max_chain(words)
    sys.stdout.write(str(result) + '\n')

if __name__ == "__main__":
    solve()
