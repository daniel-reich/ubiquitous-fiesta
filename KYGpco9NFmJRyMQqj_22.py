
def min_removals(txt1, txt2):
    return sum([1 for x in txt1 if x not in txt2] + [1 for x in txt2 if x not in txt1])

