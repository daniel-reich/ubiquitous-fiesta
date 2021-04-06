
def distance_to_nearest_vowel(s):
    d = "aeiou"
    v = [j for j in range(len(s)) if s[j] in d]
    res = [0] * len(s)
    for k, i in enumerate(s):
        if i in d:
            res[k] = 0
        else:
            o = []
            for j in v:
                o.append(abs(k - j))
            res[k] = min(o)
    return res

