
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
def is_unprimeable(n):
    '''
    Returns 'Unprimeable', 'Prime Input' or a list of primes in ascending order
    for positive integer n as per the instructions above.
    '''
    if n > 1 and len(prime_factors(n)) == 1:
        return 'Prime Input'
​
    str_num = str(n)
    primes = []   # to store found primes in
​
    for i, digit in enumerate(str_num):
        for val in range(10):
            if int(digit) != val:
                num = int(str_num[:i] + str(val) + str_num[i + 1:])
                if num % 2 == 1 or num == 2:
                    if len(prime_factors(num)) == 1:
                        primes.append(num)  # prime number found
​
    return 'Unprimeable' if len(primes) == 0 else sorted(set(primes))

