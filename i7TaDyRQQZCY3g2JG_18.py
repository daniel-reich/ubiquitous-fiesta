
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
        
def lcm_cal(a,b):
    return a*b//gcd(a,b)    
def lcm(nums):
    lcm = 1
    for i in range(0,len(nums)):
        lcm = lcm_cal(lcm,nums[i])
    return lcm

