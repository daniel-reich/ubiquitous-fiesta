
import itertools
from itertools import combinations
​
def check_sum(lst, n):
​
  Duets = list(combinations(lst,2))
  
  Counter = 0
  Length = len(Duets)
  
  while (Counter < Length):
    
    Pair = Duets[Counter]
    Total = sum(Pair)
    
    if (Total == n):
      return True
    else:
      Counter += 1
  
  return False

