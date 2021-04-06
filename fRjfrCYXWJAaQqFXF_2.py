
from functools import reduce
def is_prime(p):
    if p==2:
        #print ('Hey')
        return True
    for i in range(2,(p//2)+1):
        if p%i==0:
            return False
    return True
​
​
​
def primorial(n):
    i=2
    L=[]
    while n>0:
        while not is_prime(i):
            #print (is_prime(i))
            i+=1
        #i+=1
        L.append(i)
        i+=1
        n-=1
    return reduce(lambda x,y:x*y,L)

