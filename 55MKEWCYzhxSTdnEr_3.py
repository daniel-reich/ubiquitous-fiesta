
def gcd(a,b):
    if a==b:
        return int(a)
    elif a < b:
        return gcd(a,b-a)
    else:
        return gcd(a-b, b)

