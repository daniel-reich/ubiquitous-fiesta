
def prime_factors(num):
    return [p for p in range(2,num//2+1) if num%p==0 and all(p%ii!=0 for ii in range(2,p//2+1))]
def c_fuge(n, k, factors=[]):
    factors = factors or prime_factors(n)
    if n<1 or k==1 or k<0 or not factors and n!=k:
        return False
    k = k if k < n/2 else n-k #balacing holes instead of items if necesary
    return n==k or k==0 or any(c_fuge(n, k-factor, factors) for factor in factors)

