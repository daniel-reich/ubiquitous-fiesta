
def covered_integers(lst):
    ansset = set()
    for beg, end in lst:
        for x in range(beg, end+1):
            ansset.add(x)
    return len(ansset)

