
is_prime = lambda n: n > 1 and (n == 2 or (n%2 != 0 and all(n%ii for ii in range(3, int(n**0.5 + 1), 2))));
​
def product_of_primes(num):
    for i in range(2, int(num**0.5+1)):
        f, r = divmod(num, i)
        if r == 0 and is_prime(i) and is_prime(f):
            return True
    return False

