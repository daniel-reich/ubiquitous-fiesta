
def smith_type(number):
    if is_prime(number):
        return "Trivial Smith"
    elif not is_smith(number):
        return "Not a Smith"
    elif is_smith(number + 1):
        return "Youngest Smith"
    elif is_smith(number - 1):
        return "Oldest Smith"
    else:
        return "Single Smith"
​
def sum_of_prime_factors(num):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43 ]
    prime_factors = []
​
    while sum(k for k in primes if num % k == 0) != 0:
        i = 0
        while i < len(primes):
            if num % primes[i] == 0:
                prime_factors.append(primes[i])
                num /= primes[i]
            i += 1
    if num != 1:
        prime_factors.append(round(num)) 
    return sum(prime_factors)
​
def is_prime(num):
    return (sum((i for i in range(2, round((num / 2) + 1)) if num % i == 0 )) == 0) and num > 1
​
def digital_root(num):
    while num > 9:
        num = sum([int(i) for i in str(num)])
    return num
​
def is_smith(num):
    return (digital_root(num) == digital_root(sum_of_prime_factors(num))) and not is_prime(num)

