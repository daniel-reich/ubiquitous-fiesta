
import math
def is_exact(n, i=2):
    if n == 1:
        return [math.factorial(i-1), i-1]
    if n % i != 0:
        return 'Not exact!'
    return is_exact(n // i, i+1)

