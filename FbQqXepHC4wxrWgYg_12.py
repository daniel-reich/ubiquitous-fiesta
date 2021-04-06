
def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def prime_divisors(n):
    x=[]
    i=2
    while i<=n:
        if n%i==0:
            if isprime(i):
                x.append(i)
        i=i+1
    return x

