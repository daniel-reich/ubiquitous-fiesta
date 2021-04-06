
def unique_styles(albums):
    lista = []
    lista2 = []
    x = [element for element in albums]
    for letter in x:
        for let in letter:
            lista.append(let)
        lista.append(',')
    joined = ''.join(lista)
    splitedjoined = joined.split(",")
    return len(set(splitedjoined[0:-1]))

