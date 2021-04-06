
def validate_swaps(lst, txt):
    res = []
    for word in lst:
        if len(word) > len(txt) or sorted(word) != sorted(txt):
            res.append(False)
            continue
        letters, s = list(word), list(txt)
        indexes = [word.index(c) for c in txt if txt.index(c) != word.index(c)]
        if len(indexes) > 2 or len(indexes) < 2:
            res.append(False)
            continue
        letters[indexes[0]], letters[indexes[1]] = letters[indexes[1]],letters[indexes[0]]
        if letters == s:
            res.append(True)
        else:
            res.append(False)
    return res

