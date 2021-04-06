
def is_sorted(words, alphabet):
    d = {c: i for i, c in enumerate(alphabet)}
    return words == sorted(words, key=lambda w: [d[c] for c in w])

