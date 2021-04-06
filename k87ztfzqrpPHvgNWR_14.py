
def widen_streets(lst, n):
    result = []
    lst = list(zip(*lst))
​
    i = 0
    while i < len(lst):
        if lst[i][-1] == " ":
            for j in range(n - 1):
                lst.insert(i, lst[i])
                i += 1
        i += 1
    for v in list(zip(*lst)):
        result.append("".join(v))
    return result

