
def prime(num):
    if num<=1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
def is_powerful(num):
    d=[]
    r=[]
    s=[]
    for i in range(2,num+1):
        if prime(i):
            d.append(i)
    for j in d:
        if num%j==0:
            s.append(j)
            
    for i in d:
        t=i**2
        if num%t==0:
            r.append(t)
          
    if len(r)==len(s):
        return True
    else:
        return False

