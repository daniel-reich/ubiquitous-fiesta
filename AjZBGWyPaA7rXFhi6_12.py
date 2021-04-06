
def min_swaps(st1,st):
    l1=[]
    for i in range(len(st)):
        if st1[i]!=st[i]:
            l1.append(i)
    return int(len(l1)/2)

