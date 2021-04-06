
def bonacci(N, k):
    if N > k:
        return 0
    l = [0 for x in range(N - 1)] + [1]
    for x in range(N, k):
        l.append(sum(l[x - N: x]))
    return l[-1]

