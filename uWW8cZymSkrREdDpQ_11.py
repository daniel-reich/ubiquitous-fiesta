
def sums_up(lst):
    a = set()
    ans = []
    for x in range(len(lst)):
        target = 8-lst[x]
        if target in a:
            ans.append(sorted([target,lst[x]]))
        else:
            a.add(lst[x])
    return {'pairs': ans}

