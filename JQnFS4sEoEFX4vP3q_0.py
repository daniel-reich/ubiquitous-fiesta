
def product_pair(lst, k):
    if k>len(lst):
        return None
    else:
        lst.sort()
        pa=[]
        for i in range(0,k+1):
            p=1
            for n in lst[0:i]+[lst[-ctr-1] for ctr in range(0,k-i)]:
                p=p*n
            pa.append(p)
        return (min(pa),max(pa))

