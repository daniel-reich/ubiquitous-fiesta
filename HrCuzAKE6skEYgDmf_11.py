
import math
​
def pairs(lst):
  left  = lst[:math.ceil(len(lst)/2)];
  right = lst[math.floor(len(lst)/2):];
  return [list(tple) for tple in zip(left , right[::-1]) ];

