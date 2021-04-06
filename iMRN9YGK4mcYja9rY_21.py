
def accumulating_product(l):
    i = 0
    acc = 1
    l2 = []
    while True:
        if len(l) == 0:
            break
        for i in range(i,i+1):
            acc*=l[i]
        l2.append(acc)
        i+=1
        if i == len(l):
            break
    return l2

