
def is_parsel_tongue(sentence):
    return all('ss' in w for w in sentence.lower().split() if 's' in w)

