
def count_same_ends(txt):
    import string
    txt = txt.translate(str.maketrans('', '', string.punctuation))
    return sum(1 for x in txt.lower().split() if len(x) > 1 and x[0] == x[-1])

