
def is_prime(n):
    return n > 1 and all(n % i for i in range(2, 1+int(n**.5)))
​
​
def is_exactly_three(n):
    return is_prime(int(n ** .5)) and (n**.5) % 1 == 0

