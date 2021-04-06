
def is_sorted(words, alphabet):
    new_order = sorted(words, key=lambda x: [alphabet.index(i) for i in x])
    return words == new_order

