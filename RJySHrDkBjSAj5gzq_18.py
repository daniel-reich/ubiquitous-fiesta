
from math import factorial as fact
def nespers(lst):
    v=-1;r=1
    exp=str(lst)
    nest=[0]*exp.count('[')
    for i in exp:
        if i=='[':
            v+=1
        elif i==']':
            r*=fact(nest[v]+1)
            nest[v]=0
            v-=1
        elif i==',':
            nest[v]+=1
    return r

