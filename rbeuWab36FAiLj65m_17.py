
def grouping(w):
    d = {}
    for word in w:
        C = sum(1 for j in word if j.isupper())
        if C in d.keys():
            d[C] = sorted(d[C]+[word], key=lambda x: x.lower())
        else:
            d.update({C: [word]})
    return d

