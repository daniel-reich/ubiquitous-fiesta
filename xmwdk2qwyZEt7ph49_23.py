
def get_length(lista):
    contador = 0
    for x in lista:
        if type(x) == list:  
            contador += get_length(x)
        else:
            contador += 1    
    return contador
​
lista=[1, [2, [3, [4, [5, 6]]]]]
contador = get_length(lista)
print(contador)

