
def isprime(a):
    for i in range(2,a):
        if a%i==0:return False
    return a>1
def fat_prime(a, b):
    for i in range(max(a,b),min(a,b),-1):
        if(isprime(i)):return i

