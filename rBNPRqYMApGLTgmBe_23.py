
def combinations(k, n):
    numerator, denominator = 1, 1
    for i in range(n - k + 1, n + 1):
        numerator *= i
    for i in range(1, k + 1):
        denominator *= i
    return int(numerator / denominator)

