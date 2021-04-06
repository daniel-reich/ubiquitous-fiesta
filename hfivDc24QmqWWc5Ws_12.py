
def eratosthenes(n):
    if n == 0 or n == 1:
        return []
    prime = [True for i in range(n + 1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    return [p for p in range(n + 1) if prime[p]]

