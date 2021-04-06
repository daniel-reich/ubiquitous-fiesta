
def simplify_sqrt(n):
    max_square = max(i for i in range(1, int(n**0.5) + 1) if not n%i**2)
    return max_square, n / max_square**2

