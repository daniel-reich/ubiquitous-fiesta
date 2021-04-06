
def no_strangers(txt):
    s = ''.join(c for c in txt.lower() if c.isalpha() or c in [' ', "'"]).split()
    words = {w: 0 for w in s}
    res = [[], []]
    for word in s:
        words[word] += 1
        if words[word] == 3:
            res[0].append(word)
        elif words[word] == 5:
            res[1].append(res[0].pop(res[0].index(word)))
    return res

