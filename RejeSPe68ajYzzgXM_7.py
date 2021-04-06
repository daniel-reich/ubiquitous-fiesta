
def combine(lst):
    d = {}
    state_lst = []
    res = []
​
    for i in range(len(lst)):
        state_lst.append(lst[i][0])
​
    state_lst = sorted(set(state_lst))
​
    for state in state_lst:
        for i in range(len(lst)):
            if lst[i][0] == state:
                res.append(lst[i][-1])
​
        d[state] = res[:]
        res.clear()
​
    return d

