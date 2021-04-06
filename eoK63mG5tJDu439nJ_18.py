
def check_link(w1, w2):
    l1, l2 = len(w1), len(w2)
    if abs(l1 - l2) > 1:
        return False
    if l1 == l2:
        return sum([w1[i] != w2[i] for i in range(l1)]) == 1
    if l1 < l2:
        w1, w2 = w2, w1
    w1, w2 = list(w1), list(w2)
    for k in range(l1):
        w3 = w1[:]
        w3.pop(k)
        if w3 == w2:
            return True
    return False
​
def isWordChain(words):
    return all([check_link(words[i], words[i-1]) for i in range(1, len(words))])

