
def combinations(k, n):
# combination: 
# n!/(n-k)!k!
​
    n_factorial = 1
    nminusk = 1
    k_factorial = 1
    #factorial
    for num in range(1,n+1):
        n_factorial = n_factorial*num
    for num in range(1,(n-k)+1):
        nminusk = nminusk*num
    for num in range(1,k+1):
        k_factorial = k_factorial*num
    return ((n_factorial)/((nminusk)*k_factorial))

