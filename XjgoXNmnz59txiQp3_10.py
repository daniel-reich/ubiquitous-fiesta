
from itertools import combinations_with_replacement
import numpy as np
def split(number):
  lst, candidates = [i+1 for i in range(number)],[number]
  rr= 1 if number<=10 else 2.5 if (number >10 and number<=20) else 2.7
  for j in range (1,int((number+1)/rr)):
    for i in (list (combinations_with_replacement(lst,j))):
      if sum(i)==number:
        candidates.append(np.prod(np.array(i)))
  return (max(candidates))

