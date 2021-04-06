
def is_early_bird(limit, n):
    seq = ''.join(str(i) for i in range(limit+1))
    L, n_str, j, l_str = [], str(n), 0, len(str(n))
    while seq.find(n_str, j) != -1:
        temp = []
        start = seq.find(n_str, j)
        for k in range(l_str):
            temp.append(start+k)
        j = start + 1
        L.append(temp)
    if len(L) > 1:
        L.append('Early Bird!')
    return L

