
import itertools
def three_sum(lst):
  c=[]
  for subset in itertools.combinations(lst, 3):
    if sum(list(subset))==0:
      if list(subset) not in c:
        c.append(list(subset))
  return c

