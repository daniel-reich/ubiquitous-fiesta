
def gcd(a,b):
    g=1
    for i in range(2,a+1):
        if(b%i==0 and a%i==0):
            g=i
    return g
def lcm(a, b):
    return int((a*b)/gcd(a,b))

