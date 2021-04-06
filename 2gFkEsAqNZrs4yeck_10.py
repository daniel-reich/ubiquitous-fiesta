
def mini_peaks(lst):
    res = []
    for i in range(1, len(lst) - 1):
        group = (lst[i - 1], lst[i], lst[i + 1])
        if group[1] > group[0] and group[1] > group[2]:
            res.append(group[1])
    return res

