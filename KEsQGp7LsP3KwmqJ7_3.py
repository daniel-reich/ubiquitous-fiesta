
def check(lst):
    S = sorted(lst)
    if S == lst:
        return 'NO'
    for k in range(1, len(lst) - 1):
        if lst == S[k:] + S[:k]:
            return 'YES'
    return 'NO'

