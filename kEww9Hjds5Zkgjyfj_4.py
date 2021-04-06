
def replace_next_largest(lst):
    res = []
    for l in lst:
        for s in sorted(lst):
            if l == max(lst):
                res.append(-1)
                break
            elif l < s:
                res.append(s)
                break
    return res

