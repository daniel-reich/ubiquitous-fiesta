
def can_find(bigrams, words):
    return all(b in ' '.join(words) for b in bigrams)

