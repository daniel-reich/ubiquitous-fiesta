
def gcd(a,b):
    return max(j for j in [i for i in range(1,min(a,b)+1) if min(a,b)%i==0] if max(a,b)%j==0)

