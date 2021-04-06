
def prime_factors(n):
    i=0;primes=[]
    while i*i<n:
        i+=2
        while n%i==0:
            primes.append(i)
            n//=i
        if i==2:i=1
    if n>1:primes.append(n)
    return (sum(primes),sum(set(primes)))
            
def ruth_aaron(n):
    place=[0,9,16,1,4,10,20]
    result=(False,['Aaron',1],['Ruth',1],['Aaron',2],['Ruth',2],['Aaron',3],['Ruth',3])
    s=[prime_factors(a) for a in range(n-1,n+2)]
    choice=(s[0][0]==s[1][0])+4*(s[1][0]==s[2][0])+9*(s[0][1]==s[1][1])+\
            16*(s[1][1]==s[2][1])
    return result[place.index(choice)]

