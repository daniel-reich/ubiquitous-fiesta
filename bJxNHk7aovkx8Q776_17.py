
def gold_distribution(gold):
    a = 0
    b = 0
​
    while len(gold) > 1:
        if gold[0] >= gold[-1]:
            a += gold.pop(0)
        else:
            a += gold.pop(1)
​
        if gold[0] >= gold[-1]:
            b += gold.pop(0)
        else:
            b += gold.pop(1)
​
    return [a,b]

