
import math
​
def binomial_coefficient(n, k):
    return 0 if k > n else math.factorial(n) // (math.factorial(n - k) * math.factorial(k))
​
def lucky_ticket(n_digits):
    ans = 0
    n = n_digits // 2
    sign = -1
    for q in range(n):
        sign *= -1
        ans += binomial_coefficient(2 * n, q) * sign * binomial_coefficient(11 * n - 10 * q - 1, 2 * n - 1)
    return ans

