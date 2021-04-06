
from itertools import combinations_with_replacement
def football(score):
  scores,counter,iterr=[2, 3, 6, 7, 8],0,0
  while (iterr < score//min(scores)+1):
    for e in set(list(combinations_with_replacement(scores,iterr))):
      if sum(e)==score:
        counter+=1
    iterr+=1
  return counter

