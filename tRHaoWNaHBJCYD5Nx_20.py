
def same_letter_pattern(txt1, txt2):
    if len(txt1) != len(txt2): return False
    z = zip(txt1, txt2)
    d = dict()
    for pair in z:
        if pair[0] not in d:
            d[pair[0]] = pair[1]
        elif pair[0] in d and d[pair[0]] != pair[1]:
            return False
    return True

