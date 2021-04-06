
def gcd(a,b):
    if a == 0:
        return b
    return gcd(b % a, a)
​
​
def findlcm(a,b):
    return (a*b) // gcd(b % a, a)
​
def lcm_three(num):
    a = num[0]
    b = num[1]
​
    lcm = findlcm(a,b)
    for i in range(2,len(num)):
        lcm = findlcm(lcm,num[i])
​
    return lcm

