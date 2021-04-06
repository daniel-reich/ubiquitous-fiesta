
import math
​
def primes_below_num(n):
    list = []
    i = 0
    for j in range(2,n+1):
        for k in range(2,math.floor(math.sqrt(j))+1):
            if j % k == 0:
                i += 1
        if i == 0:
            list += [j]
            i = 0
        else:
            i = 0
    return list

