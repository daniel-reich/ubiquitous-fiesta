
def gcd(a, b):
    return [i for i in range(1,a+1) if a%i == 0 and b%i == 0][-1]

