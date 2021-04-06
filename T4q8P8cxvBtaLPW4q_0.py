
def is_prime(p):
    return p > 1 and all(p%ii != 0 for ii in range(2, int(p**0.5 +1)))
​
def extract_primes(num):
    strnum = str(num)
    return sorted(int(strnum[start: start +size]) 
        for size in range(1, len(strnum) +1)
        for start in range(len(strnum) -size +1)
        if strnum[start] != '0' and is_prime(int(strnum[start: start +size])))

