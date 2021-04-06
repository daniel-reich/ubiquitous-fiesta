
def simplify_sqrt(n):
    a, b = 1, 1
    divisor = 2
    while n > 1:
        n_divisor = 0
        while not n % divisor:
            n //= divisor
            n_divisor += 1
        a *= divisor ** (n_divisor // 2)
        b *= divisor ** (n_divisor % 2)
        divisor += 1 if divisor == 2 else 2
    return a, b

