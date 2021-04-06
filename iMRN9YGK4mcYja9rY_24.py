
def accumulating_product(lst):
    niz2 = []
    for i in range(1,len(lst)+1):
        prz = 1
        for j in range(len(lst[0:i])):
           prz*=lst[j]
        niz2.append(prz)
    return niz2;

