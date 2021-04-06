
import math
​
def binomial_coefficient(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
​
def Formula(n):
    if n == 0:
        return "1"
    ans = ""
    negative = False
    if n < 0:
        negative = True
        ans += "1/("
        n = -n
    for k in range(n, -1, -1):
        coeff = binomial_coefficient(n, k)
        if coeff > 1:
            ans += str(coeff)
        if k > 0:
            ans += "a"
        if k > 1:
            ans += "^" + str(k)
        if k < n:
            ans += "b"
        if k < n - 1:
            ans += "^" + str(n - k)
        if k > 0:
            ans += "+"
    if negative:
        ans += ")"
    return ans

