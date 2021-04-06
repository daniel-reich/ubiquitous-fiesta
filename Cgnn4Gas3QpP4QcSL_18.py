
import sys
sys.setrecursionlimit(100000)
def sum_digits_in_range(n):  
  total = 0
  
  if n == 0:    
    return total
  
  elif n == 1:
    for i in range(10):
      total += i    
    return total
​
  else:    
    return sum_digits_in_range(n-1)*10 + 45*(10**(n-1))
​
  return total

