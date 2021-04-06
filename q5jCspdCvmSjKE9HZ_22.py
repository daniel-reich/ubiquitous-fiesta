
def gcd(a,b):
    return a if b==0 else gcd(b,a%b)
def lcm_of_list(numbers):
    ans=numbers[0]
    for i in range(1,len(numbers)):
        ans=ans*numbers[i]//gcd(ans,numbers[i])
    return ans

