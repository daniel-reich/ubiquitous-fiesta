
def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)
def lcmpair(a,b):
    return a*b/gcd(a,b)
​
def lcm(nums):
    a=nums[0]
    for i in nums:
        a=lcmpair(a,i)
    return int(a)

