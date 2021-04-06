
def probability(lst, n):
    a = [x for x in lst if x >= n]
    return round((len(a)/len(lst))*100, 1)

