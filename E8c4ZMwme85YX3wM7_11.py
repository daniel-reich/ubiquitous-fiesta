
def recaman(n):
    if n == 0:
        return "---> Recaman's sequence: " + str([]) + "\n" + "---> Duplicates for n = " + str(0) + ": " + str([])
    if n == 1:
        return "---> Recaman's sequence: " + str([0]) + "\n" + "---> Duplicates for n = " + str(1) + ": " + str([])
    seq = [0]
    dups = []
    length = 0
    while length < n - 1:
        length += 1
        last = seq[-1]
        diff = last - length
        if diff > 0 and diff not in seq:
            el = diff
        else:
            el = length + last
        if el in seq and el not in dups:
            dups.append(el)
        seq.append(el)
    ans = "---> Recaman's sequence: " + str(seq) + "\n" + "---> Duplicates for n = " + str(n) + ": " + str(dups)
    return ans

