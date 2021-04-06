
def prime_factors(n):
    factors = []
    for i in range(2, int(n ** .5) + 1):
        while not n % i:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
​
​
def lcm(nums):
    factors = []
    for num in nums:
        if 1 < num < 4:
            factors.append([num])
        else:
            factors.append(prime_factors(num))
    while len(factors) > 1:
        for x in factors[0]:
            if x in factors[1]:
                factors[1].remove(x)
        factors[0] += factors[1]
        factors.pop(1)
    total = 1
    for factor in factors[0]:
        total *= factor
    return total

