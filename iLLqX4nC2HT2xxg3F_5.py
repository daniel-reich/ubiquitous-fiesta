
def deepest(lst):
    k=hi=0
    for i in str(lst):
        if i=='[':
            k+=1
        if i==']':
            k-=1
            if k>hi:
                hi=k
    return hi+1

