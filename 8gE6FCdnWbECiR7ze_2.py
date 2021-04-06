
def digital_root(n):
    '''
    Repeatedly sums the digits of positive integer n until only a
    single digit emerges.
    '''
    return n if n < 10 else digital_root(sum(int(d) for d in str(n)))
​
def is_prime(n):
    '''
    Returns True if n is prime
    '''
    return n > 1 and all(n%i for i in range(2, int(n**0.5 + 1)))
​
def prime_factors(n):
    '''
    Returns a list of the prime factors of integer n as per above
    '''
    primes = []
    for i in range(2, int(n**0.5) + 1):
​
        while n % i == 0:
            primes.append(i)
            n //= i
​
    return primes + [n] if n > 1 else primes
​
def is_smith(n):
    '''
    Returns True if n is a Smith number other than a Trivial Smith(prime)
    '''
    return not is_prime(n) and digital_root(n) == digital_root(sum(prime_factors(n)))
​
def smith_type(n):
    '''
    Returns the Smith type of positive integer n - rules as above
    '''
    if is_prime(n):
        return 'Trivial Smith'
​
    if is_smith(n):
        if is_smith(n - 1):
            return 'Oldest Smith'
        elif is_smith(n + 1):
            return 'Youngest Smith'
        else:
            return 'Single Smith'
    else:
        return 'Not a Smith'

