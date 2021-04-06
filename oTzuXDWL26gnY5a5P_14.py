
def isprime(num):
    if num < 2:
        return False
    elif num < 4:
        return True
    for x in range(2, num-1):
        if num // x == num / x:
            return False
    return True
​
def prime_numbers(num):
    return sum([1 if isprime(x) else 0 for x in range(num)])

