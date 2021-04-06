
from math import sqrt
def ecg_seq_index(n):
    d={}
    for x in range(2,500,1):
        f=[]
        for i in range(2,int(sqrt(x))+1,1):
            if x%i==0:
                f.append(i)
                f.append(int(x/i))
        if f==[]:
            f.append(x)
        d.update({x:f})
    ecg=[1,2]
    while True:
        for a in range(2,500,1):
            if a not in ecg:
                if not set(d.get(ecg[-1])).isdisjoint(set(d.get(a))):
                    ecg.append(a)
                    if a==n:
                        return len(ecg)-1
                    else:
                        break

