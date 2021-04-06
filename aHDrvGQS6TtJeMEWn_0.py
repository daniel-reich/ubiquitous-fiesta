
def max_sum_pair(lst):
    rec = 0
    n = len(lst)
    for i in range(n):
        for j in range(i, n):
            for k in range(j+1, n):
                for l in range(k, n):
                    s1 = sum(lst[i:j+1])
                    s2 = sum(lst[k:l+1])
                    rec = max(rec, s1, s2, s1+s2)
    return rec

