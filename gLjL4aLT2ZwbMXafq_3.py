
def fair_swap(l1, l2):
    sum1, sum2 = sum(l1), sum(l2)
    if (sum1 + sum2) % 2 == 1:
        return set()
    s = (sum1 + sum2) // 2
    ans = set()
    set2 = set(l2)
    for k in l1:
        if s - sum1 + k in set2:
            ans.add((k,s - sum1 + k))
    return ans

