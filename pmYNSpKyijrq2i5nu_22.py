
import itertools
​
def darts_solver(sections, darts, target):
  possibilities = itertools.combinations_with_replacement(sections, darts)
  return ["-".join(map(str,i)) for i in possibilities if sum(i) == target]

