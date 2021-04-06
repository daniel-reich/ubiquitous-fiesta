
from collections import Counter
​
import math as mt 
  
MAXN = 100001
  
​
spf = [0 for i in range(MAXN)]
​
def sieve(): 
    spf[1] = 1
    for i in range(2, MAXN): 
          
       
        spf[i] = i 
  
    # separately marking spf for  
    # every even number as 2 
    for i in range(4, MAXN, 2): 
        spf[i] = 2
  
    for i in range(3, mt.ceil(mt.sqrt(MAXN))): 
          
     
        if (spf[i] == i): 
              
         
            for j in range(i * i, MAXN, i):  
            
                if (spf[j] == j): 
                    spf[j] = i 
​
def getFactorization(x): 
    ret = list() 
    while (x != 1): 
        ret.append(spf[x]) 
        x = x // spf[x] 
  
    return ret 
​
def is_economical(n):
    h=[]
    sieve()
    
    p=getFactorization(n)
    s=digit(n)
    d=Counter(p)
    print(d)
    
    rr=""
    for c,e in d.items():
        
        if e>1:
            rr+=str(c)+str(e)
        else:
            rr+=str(c)
    print(rr)
  
    m=len(rr)
    
    
    if m==s:
        return "Equidigital"
    elif m<s:
        return "Frugal"
    else:
        return "Wasteful"
            
    
def digit(n):
    q=str(n)
    d=[]
    for i in q:
        d.append(q)
    return len(d)

