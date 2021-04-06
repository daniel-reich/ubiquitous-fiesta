
def cycle_length(lst, n):
    lst_c = lst.copy()
    lst_c.sort()
    c = 0
    while lst.index(n) != lst_c.index(n):
​
        for i in lst:
            if lst.index(n) == lst_c.index(i):
                c += 1
                f = lst.index(n)
                m = lst.index(i)
                lst[f], lst[m] = lst[m], lst[f]
​
    return c

