
def block(lst):
    lista = [list(i) for i in list(zip(*lst)) if 2 in i]
    q = 0
    for i in lista:
        q += len(i) - (i.index(2) + 1)
    return q

