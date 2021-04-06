
from math import factorial
​
def non_repeats(num):
    # Start by calculating the total valid combinations of numbers
    # Total = n!/(n-i)!*(n-i), where n is the number given and i is the size of a 
    # sliding window inside the list of numbers.
    
    # Subtract the invalid numbers starting with 0 from all combinations. 
    # Zeros = (n-1)!/(n-i-1)!
    
    total = 0
    zeros = 0
    for i in range(num):
        combinations = factorial(num)//factorial(num-i)*(num-i)
        invalid = factorial(num-1)//factorial(num-i-1)
        total += combinations
        zeros += invalid
    
    return total-zeros

