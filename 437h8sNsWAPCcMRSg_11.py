
def product_of_primes(num):
    i = 2
    factors = []
    while num > 1:
        if num % i == 0:
            num /= i
            factors.append(i)
        else:
            i += 1
    # print(factors)
    return len(factors) == 2

