
def can_find(bigrams, words):
    return all(list(map(lambda x:any(list(map(lambda y:x in y,words))),bigrams)))

