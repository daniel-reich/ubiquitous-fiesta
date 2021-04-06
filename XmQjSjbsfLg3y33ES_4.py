
def legalbacklog(cases, m):
    lst = sorted(v for k, v in cases.items())
    len_lst = len(lst)
    days = 0
    while sum(lst) > 0:
        for idx in range(len_lst - 1, max(len_lst - m - 1, -1), -1):
            if lst[idx]:
                lst[idx] -= 1
        lst.sort()
        days += 1
    return days

