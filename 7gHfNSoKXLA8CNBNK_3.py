
def prime_factors(n):
    i=0;primes=[]
    while i*i<n:
        i+=2
        while n%i==0:
            primes.append(i)
            n//=i
        if i==2:i=1
    if n>1:primes.append(n)
    return primes        
​
def sim_prop_frac(max_den):
    k=0
    for d in range(2,max_den+1,1):
        p=set(prime_factors(d))
        for n in range(1,d,1):
            if set(prime_factors(n)).intersection(p)==set():
                k+=1
    return k

