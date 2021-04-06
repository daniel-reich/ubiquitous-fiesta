
from math import factorial
​
def Formula(n):
    if n == 0:
        return "1"
    sol = []
    m = abs(n)
    fact = 0
    x = 0
    for k in range(m+1):
        fact = factorial(m)//(factorial(k)*factorial(m-k))
        x = m - k
        sol.append("{}{}{}{}{}{}{}".format("" if fact == 0 or fact == 1 else fact, "" if x ==
                                           0 else "a", "" if x < 2 else "^", "" if x < 2 else x, "" if k ==
                                           0 else "b", "" if k < 2 else "^", "" if k < 2 else k))
    return "1/({})".format("+".join(sol)) if n < 0 else "+".join(sol)

