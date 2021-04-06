
def order(lst):
    L = [[lst[i], i] for i in range(len(lst))]
    L.sort(key = lambda x: (x[0], x[1]))
    return [el[1] for el in L]

