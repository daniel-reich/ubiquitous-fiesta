
def is_valid(txt):
    lst = sorted([txt.count(ch) for ch in set(txt)])
    c = 0
    if lst[-1] - lst[0] > 1:
        return 'NO'
    for i in range(len(lst)):
        if lst[i] != lst[0]:
            c += 1
        if c == 2:
            return 'NO'
    return 'YES'

