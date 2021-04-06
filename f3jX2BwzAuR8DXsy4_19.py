
def fact_of_fact(n):
    fact = lambda n: 1 if n<2 else n*fact(n-1)
    ans = 1
    for i in range(n,0,-1):
        ans*=fact(i)
    return ans

