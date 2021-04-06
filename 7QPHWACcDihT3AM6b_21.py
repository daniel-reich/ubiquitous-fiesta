
def can_find(bigrams, words):
    return all(bigram in ''.join(words) for bigram in bigrams)

