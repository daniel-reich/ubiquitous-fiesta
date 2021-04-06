
def custom_sort(t, s):
    seq = {}
    k = 0
    for c in t:
        seq[k] = c
        k += 1
    for c in "abcdefghijklmnopqrstuvwxyz":
        if c not in t:
            seq[k] = c
            k += 1
    ans = ""
    for i in range(26):
        ans += seq[i] * s.count(seq[i])
    return ans

