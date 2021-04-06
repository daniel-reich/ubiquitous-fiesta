
def intersection(h1, h2):
    a = h1.keys() & h2.keys()
    return [{i:h1[i]for i in a},{i:h2[i]for i in a}]

