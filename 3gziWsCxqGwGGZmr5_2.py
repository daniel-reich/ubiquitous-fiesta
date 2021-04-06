
def fat_prime(a, b):
    for i in reversed(range(min(a,b),max(a,b)+1)):
        if is_prime(i):
            return i;
    
    
def is_prime(n):
    C = 0;
    N = n;
    while N != 0:
        if n % N == 0:
            C+=1;
        N-=1;
    if C ==2:
        return True
    return False

