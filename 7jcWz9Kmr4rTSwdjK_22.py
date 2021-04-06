
def prime_factorize(num):
    def is_prime(n):
        return all(bool(n%i!=0) for i in range(2,n))
    if num == 1: return []
    for i in range(2,num+1):
        if (num%i==0) and is_prime(i):
            return [i]+prime_factorize(num//i)

