
def can_find(bigrams, words):
    nl = []
    for bi in bigrams:
        nl.append(sum(1 for w in words if bi in w))
    return nl.count(0) == 0

