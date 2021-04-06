
def sort_by_character(words, n):
    words.sort(key=lambda words: words[n - 1])
    return words

