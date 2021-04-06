
def canChain(w1, w2):
    l1, l2 = len(w1), len(w2)
    if abs(l1 - l2) > 1:
        return False
    if l1 == l2:
        return sum(1 if w1[i] != w2[i] else 0 for i in range(l1)) == 1
    if l2 > l1:
        return sum(1 if w2[i] not in w1 else 0 for i in range(l2)) <= 1
    return sum(1 if w1[i] not in w2 else 0 for i in range(l1)) <= 1
​
def isWordChain(words):
    return all(canChain(w1, w2) for w1, w2 in zip(words, words[1:]))

