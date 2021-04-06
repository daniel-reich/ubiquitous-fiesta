
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if not n%i:
            return False
    return True
​
def sexy_primes(n, limit):
    def is_in(e, lst):
        lst_c = [e+i*6 for i in range(n)]
        return all(x in lst for x in lst_c)
    
    lst = [i for i in range(2, limit) if is_prime(i)]
    return [tuple(x+i*6 for i in range(n)) for x in lst if is_in(x, lst)]

