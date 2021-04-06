
def cumulative_sum(lst):
    suma = 0
    lista = [ ]
    if lst =='':
        return []
    for a in lst:
        suma +=a
        lista.append(suma)
    return lista

