
def partitions(n, verbose=0):
    if n <= 1:
        return 1
    ctr = 0
    q = [[x] for x in range(n,0,-1)]
    while q:
        x = q.pop(0)
        sum_x = sum(x)
        if sum_x == n:
            ctr += 1
        else:
            for k in range(1, min(n-sum_x, x[-1])+1):
                q.append(x + [k])
    return ctr

