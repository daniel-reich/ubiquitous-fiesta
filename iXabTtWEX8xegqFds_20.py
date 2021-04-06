
def alternate_sort(lst):
    n = sorted(list(filter(lambda x:type(x)==int,lst)))[::-1]
    a = sorted(list(filter(lambda x:type(x)!=int,lst)))[::-1]
    res =[]
    for i in range(len(n)):
        res.append(n.pop())
        res.append(a.pop())
    return  res

