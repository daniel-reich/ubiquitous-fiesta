
def isprime(a):
    if a == 1:
        return False
    for i in range(2, int((a**0.5) + 1)):
        if a % i == 0:
            return False
    return True
​
​
def truncatable(n):
    s = str(n)
    if "0" in s:
        return False
    l, r = True, True
    x, y = s, s
    for i in range(len(s)):
        if not isprime(int(x)):
            l = False
        x = x[1:]
        if not isprime(int(y)):
            r = False
        y = y[:-1]
    if r == True and l == True or len(s) == 1:
        return "both"
    elif r == True:
        return "right"
    elif l == True:
        return "left"
    else:
        return False

