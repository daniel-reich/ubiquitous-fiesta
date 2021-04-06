
def funny_numbers(n, p):
    res = list(map(int,list(str(n))))
    ans = 0
    for i,v in enumerate(res):
        ans+=v**(i+p)
    return ans//n if ans%n==0 else None

