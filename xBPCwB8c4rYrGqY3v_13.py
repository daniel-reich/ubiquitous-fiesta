
def missing(lst):
    x = lst[-1] - lst[-2]
    lista = [i + x for i in lst]
    return [i for i in lista if i not in lst][0]

