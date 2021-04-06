
import math 
def checkSemiprime(num): 
    cnt = 0
    for i in range(2, int(math.sqrt(num)) + 1): 
        while num % i == 0: 
            num /= i 
            cnt += 1
        if cnt >= 2:  
            break
    if(num > 1): 
        cnt += 1
    return cnt == 2
def semi_prime(n): 
    if checkSemiprime(n) == True: 
        return n
def createSemiPrimeSieve(n): 
    v = [0 for i in range(n + 1)] 
    for i in range(1, n + 1): 
        v[i] = i 
    countDivision = [0 for i in range(n + 1)] 
    for i in range(n + 1): 
        countDivision[i] = 2
    for i in range(2, n + 1, 1): 
        if (v[i] == i and countDivision[i] == 2):
            for j in range(2 * i, n + 1, i): 
                if (countDivision[j] > 0): 
                    v[j] = int(v[j] / i)
                    countDivision[j] -= 1
    res = [] 
    for i in range(2, n + 1, 1):
        if (v[i] == 1 and countDivision[i] == 0): 
            res.append(i) 
    return res     
def semiprimes(n):        
    return ([i for i in range(1,n) if semi_prime(i)],createSemiPrimeSieve(n))

