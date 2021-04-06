
def letters(word1, word2):
    x = set(word1)
    y = set(word2)
    intersection = "".join(sorted(x.intersection(y)))
    diff1= "".join(sorted(x.difference(y)))
    diff2= "".join(sorted(y.difference(x)))
    return [intersection,diff1,diff2]

