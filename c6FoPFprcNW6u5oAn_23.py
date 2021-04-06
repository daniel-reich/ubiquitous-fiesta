
def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a
​
def reduce(fraction):
    num, den = [int(i) for i in fraction.split("/")]
    while gcd(num, den) > 1:
        g = gcd(num, den)
        num //= g
        den //= g
    return str(num)+"/"+str(den)
    
​
def farey(n):
    lst = ["0/1"] + [str(i)+"/"+str(j) for i in range(1,n) for j in range(1,n+1) if i<=j]
    lst = [reduce(i) for i in lst]
    return sorted(list(set(lst)), key = eval)

