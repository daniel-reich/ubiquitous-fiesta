
def is_economical(n):
    def get_prime_factors(n):
        for i in range (n - 1, 1, -1):
            if (n % i):
                continue
            j = int(n / i)
            return str(get_prime_factors(i)) + ", " + str(get_prime_factors(j))
        return n
    prime_factors = get_prime_factors(n)
    if (type(prime_factors) == int):
        prime_factors = [prime_factors]
    else: 
        prime_factors = prime_factors.split(", ")
    unique_factors = [[], []]
    for factor in prime_factors:
        if (not (factor in unique_factors[0])):
            unique_factors[0].append(factor)
            unique_factors[1].append(1)
        else:
            index = unique_factors[0].index(factor)
            unique_factors[1][index] = int(unique_factors[1][index]) + 1
    answer = 0
    for factor in unique_factors[0]:
        answer += len(str(factor))
    for expo in unique_factors[1]:
        if (int(expo) > 1):
            answer += len(str(expo))
    if (answer < len(str(n))):
        return "Frugal"
    if (answer > len(str(n))):
        return "Wasteful"
    return "Equidigital"

