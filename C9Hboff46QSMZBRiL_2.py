
def kth_string(S, M, k):
    lS, l, last, jp, s = len(S), sorted(S), 1, [1], ""
    for i in range(M-1):
        last = last*lS + 1
        jp.append(last)
    for j in jp[::-1]:
        if k:
            k -= 1
            p = k//j
            s += l[p]
            k -= p*j
        else:
            return s
    return s

