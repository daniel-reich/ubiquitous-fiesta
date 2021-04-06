
def simplify_sqrt(n):
    m,flag,fact=n,1,1    
    while flag:
        flag=0        
        for i in range(2,int(m**.5)+1):
            if n%(i**2)==0:
                fact*=i
                n//=i**2
                flag=1
                break
    return (fact,n)

