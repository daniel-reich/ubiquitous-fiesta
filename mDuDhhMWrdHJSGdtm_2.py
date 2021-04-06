
def divisible(n):
    '''
    Returns True if n has exactly 3 divisors
    '''
    divisors = {1}
    divisors.add(n)  # every number has 1 & itself as a divisor
​
    for i in range(2, int(n**0.5) + 1):
        if not n % i:
            divisors.add(i)
            divisors.add(n // i)
            if len(divisors) > 3:
                return False
​
    return len(divisors) == 3

