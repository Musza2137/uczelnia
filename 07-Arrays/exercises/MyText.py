def word_count(text):
    words = text.split()
    return len(words)


def words_longest_to_shortest(text):
    words = text.split()
    n = len(words)
    for i in range(n):
        for j in range(0, n - i - 1):
            if len(words[j]) < len(words[j + 1]):
                temp = words[j]
                words[j] = words[j + 1]
                words[j + 1] = temp
    return words


def words_alphabetical(text):
    words = text.split()
    return sorted(words)
