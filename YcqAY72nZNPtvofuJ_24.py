
def quad_sequence(lst):
    n = len(lst)
    diff1 = [lst[i] - lst[i-1] for i in range(1, n)]
    diff2 = [diff1[i] - diff1[i-1] for i in range(1, n - 1)]
    assert len(set(diff2)) == 1
    a = diff2[0] // 2
    subs = [(lst[k - 1] - a * k**2) for k in range(1, n + 1)]
    diff3 = [subs[i] - subs[i-1] for i in range(1, len(subs))]
    assert len(set(diff3)) == 1, diff3
    b = diff3[0]
    c = lst[0] - a - b #b + diff3[0]#subs[0] - lst[0]
    ans = [a*k**2 + b*k + c for k in range(n + 1, 2 * n + 1)]
    return ans

