
def num_then_char(lst):
    l = (sum(lst, []))
    result = sorted([n for n in l if not isinstance(
        n, str)]) + sorted([ch for ch in l if isinstance(ch, str)])
    sol = []
    index = 0
    for lsts in lst:
        s = []
        for item in lsts:
            s.append(result[index])
            index += 1
        sol.append(s)
​
    return sol

