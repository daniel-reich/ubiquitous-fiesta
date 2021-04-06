
# this seemed more direct than recursion to me
def num_ways(n, s):
    d = {n:1}
    for k in range(n-1, -1, -1):
        cnt = 0
        for j in sorted(s):
            cnt += d.get(k+j, 0)
        d[k] = cnt
    return d[0]

