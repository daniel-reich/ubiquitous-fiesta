
import itertools
from itertools import combinations
​
def difference_two(lst):
  
  Duets = list(combinations(lst,2))
  
  Answer = []
  
  for x in Duets:
    Test = abs(x[1] - x[0])
    if (Test == 2):
      Answer.append(sorted(list(x)))
  
  Answer = sorted(Answer)
  
  return Answer

