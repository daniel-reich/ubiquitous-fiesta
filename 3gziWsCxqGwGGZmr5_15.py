
is_prime = lambda n: n > 1 and all(n%i for i in range(2, int(n**0.5 + 1)))
​
def fat_prime(a, b):
    '''
    Returns the largest prime in the range (a, b) where a and b are +ve integers
    '''
    for i in range(max(a,b),min(a,b)-1,-1):
        if is_prime(i):
            return i
​
    return "Ooer! There ain't one in this range!!"

