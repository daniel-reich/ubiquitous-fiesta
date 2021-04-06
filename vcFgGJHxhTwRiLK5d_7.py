
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
​
def lcm(x, y):
    return abs(x * y) // gcd(x, y)
​
def smallest(n):
    res = 1
    for i in range(1, n + 1):
        res = lcm(res, i)
    return (res)

