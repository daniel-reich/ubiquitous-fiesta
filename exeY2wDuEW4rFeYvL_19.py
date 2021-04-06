
def ordered_matrix(a, b):
    rang3 = a*b + 1    
    lst = []
    lst_r = []
    for m in range(1, (rang3)):
        if len(lst_r) == b:
            lst.append(lst_r)
            lst_r = []
            lst_r.append(m)
        elif len(lst_r) <= b:
            lst_r.append(m)
    lst.append(lst_r)
    return lst

