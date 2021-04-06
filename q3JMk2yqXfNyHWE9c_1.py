
def double_letters(word):
    return any(c1 == c2 for c1, c2 in zip(word, word[1:]))

