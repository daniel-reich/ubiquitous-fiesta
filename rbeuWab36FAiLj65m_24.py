
def grouping(w):
    d = {}
    for word in w:
        cnt = len([c for c in word if 'A' <= c <= 'Z'])
        if cnt not in d:
            d[cnt] = [word]
        else:
            d[cnt].append(word)
    for key in d:
        words = [[w, w.lower()] for w in d[key]]
        words.sort(key=lambda x: x[1])
        d[key] = [w[0] for w in words]
    return d

