
def min_removals(txt1, txt2):
    s = 0
    for i in txt1:
        if i not in txt2:
            s += 1
    for x in txt2:
        if x not in txt1:
            s += 1
    return s

