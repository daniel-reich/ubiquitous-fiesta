
def check(lst, rest):
    if lst == [] and rest == [0,0,0]:
        return True
    for i in (0,1,2):
        if rest[i] >= lst[0]:
            new_rest = rest.copy()
            new_rest[i] -= lst[0]
            if check(lst[1:], new_rest):
                return True
    return False
​
def coins_div(lst):
    s = sum(lst)
    if s%3:
        return False
    else:
        s //= 3
    if max(lst) > s:
        return False
    return check(lst[1:], [s-lst[0], s, s])

