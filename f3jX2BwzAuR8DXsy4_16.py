
fac = {0: 1, 1: 1}
f = 1
for k in range(2, 51):
    f *= k
    fac[k] = f
​
def fact_of_fact(n):
    ans = 1
    for k in range(2, n + 1):
        ans *= fac[k]
    return ans

