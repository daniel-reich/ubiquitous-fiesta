
def find_longest(sentence):
    return sorted(sentence.lower().replace(".","").replace("'s","").replace(",","").split(), key=len)[-1]

