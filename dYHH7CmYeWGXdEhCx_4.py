
def word_builder(letras, numeros):
    lista = set(zip(numeros, letras))
    b = sorted(lista)
    numeros1, letras1 = zip(*b)
    return ''.join(letras1)

