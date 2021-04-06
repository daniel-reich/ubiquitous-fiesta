
def gcd_order(a, b):
    if b % a == 0:
        return a
    else:
        return gcd_order(b % a, a)
​
​
def gcd(a, b):
    if a > b:
       return gcd_order(b, a)
    return gcd_order(a, b)

