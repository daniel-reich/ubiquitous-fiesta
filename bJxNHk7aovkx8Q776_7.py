
def gold_distribution(gold):
    res, idx = [0, 0], 0
    while gold:
        if gold[0] >= gold[-1]:
            res[idx] += gold[0]
            gold = gold[1:]
        else:
            res[idx] += gold[-1]
            gold = gold[:-1]
        idx = 1 - idx
    return res

