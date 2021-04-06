
def sums_up(lst):
    res = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == 8:
                res.append([lst[i], lst[j]])
    res.sort(key=lambda x: lst.index(x[1]))
    return {"pairs": [sorted(pair) for pair in res]}

