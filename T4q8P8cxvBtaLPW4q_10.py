
import math
def isPrime(num):
    if num == 1 or num == 0:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
#return all possible strings 
#like abcde 
#a, b, c, d, e, ab, bc, cd, de, abc, bcd, cde, abcd, bcde
def extract(num, length):
    out = []
    num = str(num)
    limit = len(num) - length 
    for i in range(limit + 1):
        out.append(num[i:i + length])
    return out
def extract_primes(num):
    num = str(num)
    output = []
    primes = []
    for i in range(1, len(num) + 1):
        output.append(extract(num, i))
    print(output)
    for lst in output:
        #print(lst)
        
        for e in lst:
            if e[0] == '0':
                continue
            if isPrime(int(e)):
                primes.append(int(e))
    return sorted(primes)
​
def remDupe(lst):
    for e in range(len(lst)):
        if lst.count(lst[e])  == 1:
            if e == len(lst) - 1:
                return lst
            #print(lst)
            continue
        else:
            del lst[e]
            remDupe(lst)
    return lst

