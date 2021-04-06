
import itertools as i
def clear_ordering(lst):
  p = i.permutations(set(i.chain.from_iterable(lst)))
  g = iter([[x[i], x[i+1]] for i in range(len(x)-1)] for x in p)
  return any(all(pairs in lst for pairs in group) for group in g)

