
def fruit_salad(fruits):
    k=[]
    for i in fruits:
       m=len(i)//2
       k+=[i[:m],i[m:]]
    return ''.join(sorted(k))

