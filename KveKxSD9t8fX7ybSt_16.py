
def final_countdown(lst):
    res = []
    begin = 0
    for idx, val in enumerate(lst):
        if val == 1:
            if idx > 0 and lst[idx - 1] == 2:
                res.append(lst[begin: idx + 1])
            else:
                res.append([1])
            begin = idx + 1
        elif idx > 0 and val + 1 != lst[idx - 1]:
            begin = idx
    return [len(res), res]

