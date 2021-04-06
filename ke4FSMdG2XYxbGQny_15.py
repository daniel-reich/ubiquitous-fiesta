
def even_odd_transform(lst, n):
    b=[]
    i=0
    for i in range(len(lst)):
        if lst[i]%2 == 0:
            b.append(lst[i]-(2*n))
        else:
            b.append(lst[i]+(2*n))
    return b

