
import itertools as iter
def darts_solver(sections, darts, target):
  db = list(iter.product(sections,repeat=darts))
  sumdb = [sum(i) for i in list(db)]
  indices = [i for i, x in enumerate(sumdb) if x == target]
  tupleresults = map(tuple,sorted([list(i) for i in set(map(tuple,  [sorted(i) for i in [db[i] for i in indices]]))]))
  return [(['-'.join([str(i) for i in n])][0]) for n in tupleresults] if target in sumdb else []

