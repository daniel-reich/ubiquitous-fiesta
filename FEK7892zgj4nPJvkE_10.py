
def primes_lst(nbr):
    primes=[2,3]
    for i in range(4,nbr + 1):
        prime_fnd = True
        for p in primes:
            if i%p == 0:
                prime_fnd = False
                break 
        if prime_fnd:
            primes.append(i)
    return primes
P = primes_lst(500)
​
def prime_gaps(gap, start1, end1):
    for indx, prime in enumerate(P):
        ##print ((gap,start1,end1,indx,prime))
        if  prime > end1:
            break
        if  prime >= start1 and P[indx + 1] <= end1 and P[indx+1] - prime == gap:
            return [prime, P[indx + 1]]

