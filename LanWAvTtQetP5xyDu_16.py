
def coins_div(lst):
    a = sum(lst)/3
    m = a
    s = []
    c = len(lst)
    d = len(lst) * len(lst)
    while len(lst) > 0:
        for z in range(0, len(lst)+1):
            for x in (lst[z:len(lst)]+ lst[0:z]):
                if x != m:
                    if m - x > 0:
                        m = m - x
                        s.append(x)
                        lst.remove(x)
                        c = c - 1
                        continue
                    if (m - x) < 0:
                        lst = lst + s
                        s = []
                        m = a
                        c = c - 1
                if x == m:
                    m = a
                    lst.remove(x)
                    s = []
                    c = c - 1
                if c <= 0:
                    d = d -1
                    break
            if d <= 0:
                break
        if d <= 0:
            break
    if len(lst) == 0:
        return True
    else:
        return False

