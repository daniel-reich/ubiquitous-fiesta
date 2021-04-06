
def recaman_index(n):
    lst = [0]
    while lst[-1] != n:
        x, y = lst[-1], len(lst)
        if x > y and x - y not in lst:
            lst.append(x - y)
        else:
            lst.append(x + y)
    return lst.index(n)

