
import math
def simplify_sqrt(n):
    square_factors = [r for r in range(1, int(math.sqrt(n)) + 1) if n % r**2 == 0]
    return square_factors[-1], n // square_factors[-1]**2

