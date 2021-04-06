
def fat_prime(a, b):
    is_prime = lambda n: n==2 or n>1 and n%2 and all(n%i for i in range(3,int(n**.5)+1,2))
    a,b = sorted([a,b])
    b = b - (b%2==0)
    while a<b:
        if is_prime(b):
            return b
        b -=2

