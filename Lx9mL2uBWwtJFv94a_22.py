
def checker_board(n, el1, el2):
    lista,lista2 = [], []
    while len(lista) < n:
        lista.append(el1)
        lista2.append(el2)
        if len(lista) == n:
            break
        lista.append(el2)
        lista2.append(el1)
    lista3 = []
    while len(lista3) < n:
        lista3.append(lista)
        if len(lista3) == n:
            break
        lista3.append(lista2)
    if el1 == el2:
        return 'invalid'
    return lista3

