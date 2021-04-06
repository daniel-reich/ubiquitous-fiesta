
def pricey_prod(d):
    lst,lst1,lst2=[],[],[]
    for i in d:
        if d.get(i)>499:
            lst.append(i)
            lst1.append(d.get(i))
    for j in range(0,len(lst)):
        k=sorted(lst1)[::-1].index(lst1[j])
        lst2.append(lst[k])
    return lst2

