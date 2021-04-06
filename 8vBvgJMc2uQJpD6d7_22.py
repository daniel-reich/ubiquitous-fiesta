
def prime_factors(n):
    primes = []   
    
    while n % 2 == 0: #while n is even
        primes += 2, #add 2 to list
        n = n / 2 #divide by 2
    
    for i in range(3, int(n**0.5) + 1, 2): 
        while n % i== 0: 
            primes += int(i), 
            n = n / i 
    
    if n > 2: 
        primes += int(n),
        
    return primes

