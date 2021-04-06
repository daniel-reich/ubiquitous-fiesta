
def abbreviate(sentence, n=4):
    return ''.join(w[0].upper() for w in sentence.split() if len(w) >= n)

