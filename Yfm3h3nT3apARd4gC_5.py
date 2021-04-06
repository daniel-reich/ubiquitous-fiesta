
def rolls(lst):
    out = list(lst)
    for i in range(len(lst)-1):
        if lst[i] == 6:
            out[i + 1] = lst[i + 1] * 2
        elif lst[i] == 1:
            out[i+1] = lst[i+1]*0
    return sum(out)

