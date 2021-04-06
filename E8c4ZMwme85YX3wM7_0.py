
def recaman(n):
    found, dup = set(), []
    seq, i = [], 0
​
    for k in range(n):
        if i-k > 0 and i-k not in found:
            i -= k
        else:
            i += k
            if i in found and i not in dup:
                dup.append(i)
        found.add(i)
        seq.append(i)
        
    return "---> Recaman's sequence: {}\n---> Duplicates for n = {}: {}".format(seq, n, dup)

