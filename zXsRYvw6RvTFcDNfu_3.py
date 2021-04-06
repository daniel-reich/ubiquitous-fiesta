
from math import floor, sqrt
​
def prime_reduce(n):
    """For an integer n, return n if it is prime,
    or else its lowest divisor and the quotient"""  
    if n == 2:
        return [2]
    if n % 2 == 0:
        return [2, n // 2]
    for i in range(3, floor(sqrt(n))+1, 2): 
        if n % i == 0:
            return [i, n // i]
    return [n]
​
def reduce_list(n):
    """reduce a list to its prime factors"""
    n = [n] if isinstance(n, int) else n
    result = []
    
    for i in n:
        [result.append(j) for j in prime_reduce(i)]
    if len(result) >  len(n):
        return reduce_list(result)
    return result
    
def ruth_aaron(n):    
    """Check the Ruth-Aaron pair for the numbers adjacent to n."""
    comparisons = [-1, 1]
    name = ["Aaron", "Ruth"]
    for i, j in zip(comparisons, name):
        same_sum = sum(reduce_list(n)) == sum(reduce_list(n + i))
        same_unique_sum = sum(set(reduce_list(n))) == sum(set(reduce_list(n + i)))
        
        if same_unique_sum and same_sum:
            return [j, 3]
        elif same_sum:
            return [j, 2]
        elif same_unique_sum:
            return [j, 1]
        
    return False

