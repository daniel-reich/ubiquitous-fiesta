
"""
1. No factorial is going to have fewer zeros than the factorial 
of a smaller number.
​
2. Each multiple of 5 adds a 0, so first we count how many multiples of 5 are
  smaller than `n` (`n // 5`).
​
3. Each multiple of 25 adds two 0's, so next we add another 0 for each 
  multiple of 25 smaller than n.
​
4. We continue on for all powers of 5 smaller than (or equal to) n.
"""
def trailing_zeros(n):
    pow_of_5 = 5
    zeros = 0
    
    while n >= pow_of_5:
        zeros += n // pow_of_5
        pow_of_5 *= 5
        
    return zeros

