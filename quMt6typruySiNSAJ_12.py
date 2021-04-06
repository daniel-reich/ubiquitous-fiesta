
from math import ceil
def shuffle_count(num):
    d=[i for i in range(num)]
    ds=[0]*num
    k=0
    while True:
        d1=d[:num//2]
        d2=d[num//2:]
        for i in range(0,num-1,2):
            ds[i]=d1[ceil(i/2)]
            ds[i+1]=d2[ceil(i/2)]
        k+=1
        d=ds
        if d==sorted(d):
            return k

