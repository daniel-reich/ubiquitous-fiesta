
def prime_factorization(n):
    ans = []  
    for i in range(2, n+1): 
        while n % i == 0: 
            ans.append(i)
            n = n // i
    return ans

