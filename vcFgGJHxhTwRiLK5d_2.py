
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
​
​
def smallest(n):
    ans = 1
    for i in range(1, n + 1):
        ans = (ans * i) // gcd(ans, i)
    return ans

