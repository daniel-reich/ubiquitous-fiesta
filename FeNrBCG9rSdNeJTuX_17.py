
def max_possible(n1, n2):
    l1=list(str(n1))
    l2=sorted(list(str(n2)),reverse=True)
    for i in range(len(l1)):
        if len(l2)>0 and l1[i]<l2[0]:
            l1[i]=l2.pop(0)
    return(int(''.join(l1)))

