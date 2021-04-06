
def round_number(num, n):
    lista = [i * n for i in range(1, 2000000)]
    lista2 = sorted(list(zip([abs(num - i) for i in lista], lista)))
    if lista2[0][0] == lista2[1][0]:
        return max(lista2[0][1], lista2[1][1])
    else:
        return lista2[0][1]
​
​
# not proud

