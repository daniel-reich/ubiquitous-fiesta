
def can_complete(initial, word):
    try:
        lista = [[i, word.index(i)] for i in initial]
    except:
        return False
    return lista == sorted(lista, key=lambda x: x[1]) and all([initial.count(i) <= word.count(i) for i in initial])

