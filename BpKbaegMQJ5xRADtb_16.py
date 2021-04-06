
def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if not n % 2:
        return False
    for k in range(3, int(n ** 0.5) + 1, 2):
        if not n % k:
            return False
    return True
​
​
def is_unprimeable(num):
    if is_prime(num):
        return 'Prime Input'
    primes = set()
    num_lst = list(str(num))
    for i in range(len(num_lst)):
        new_lst = num_lst[:]
        for digit in range(10):
            new_lst[i] = str(digit)
            new_num = int(''.join(d for d in new_lst))
            if is_prime(new_num):
                primes.add(new_num)
    if primes:
        return sorted(list(primes))
    return 'Unprimeable'

