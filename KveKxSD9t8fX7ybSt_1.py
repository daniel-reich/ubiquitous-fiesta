
import itertools as i
def final_countdown(lst):
  g = i.groupby(enumerate(lst), lambda x: x[0]+x[1])
  q = list(filter(lambda l: l[-1]==1, ([b for a,b in v] for k,v in g)))
  return [len(q), q]

