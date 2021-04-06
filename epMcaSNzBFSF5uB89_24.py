
import itertools
def currently_winning(scores): 
  y = list(itertools.accumulate(scores[0::2]))
  o  = list(itertools.accumulate(scores[1::2]))
  return ['Y' if x > y else 'O' if x < y else 'T' for x, y in zip(y, o)]

