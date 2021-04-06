
def product_of_primes(num):
    i = 1
    j = 1
​
    while i * j < num:
        i = next_prime(i)
        while i*j < num:
             j = next_prime(j)
​
        if i*j == num:
            return True
        j = 2
​
    return False
​
​
def next_prime(prime):
    a = prime + 1
    while not is_prime(a):
        a += 1
    return a
​
​
def is_prime(num):
    if num == 1 or num == 0:
        return False
    i = 2
    while i < num - 1:
        if num % i == 0:
            return False
        i += 1
    return True

