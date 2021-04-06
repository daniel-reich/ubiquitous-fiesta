
from itertools import cycle
​
​
def matcher(txt, cycle):
  return sum(
    i != next(cycle)
    for i, _ in zip(txt, range(len(txt)))
  )
​
​
def min_swaps(string):
  cycles = (cycle('01'), cycle('10'))
  return min(matcher(string, i) for i in cycles)

