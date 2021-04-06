
def cons(lst):
    lst.sort()
    ini = lst[0]
    final = lst[-1]
    lst_aux = list(range(ini, final+1))
    return lst == lst_aux

