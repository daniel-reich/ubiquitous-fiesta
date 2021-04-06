
def GCD(lst):
    ans = lst[0]
    for x in lst[1:]:
        ans = gcd(ans, x)
    return ans
   
def gcd(a, b):
    if(b==0):
        return a
    else:
        return gcd(b, a%b)

