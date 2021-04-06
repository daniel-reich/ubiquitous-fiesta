
def lcm_three(num):
    pass
​
​
def gcd(x, y):
    while (y):
        x, y = y, x % y
    return x
​
​
def lcm_three(num):
    g1 = gcd(num[0], num[1])
    g2 = gcd(num[0]*num[1]//g1, num[2])
    return num[0] * num[1] * num[2] // (g1 * g2)

