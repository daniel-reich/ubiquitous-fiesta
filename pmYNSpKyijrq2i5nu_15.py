
from itertools import product
def darts_solver(sections, darts, target):
  # product creates iterable of all combinations of possible scores for given number of darts, add to set
  # to remove duplicates, filter only those which add up to target and sort in ascending order of each dart's score
  sets = sorted([t for t in set(tuple(sorted(p)) for p in product(sections, repeat=darts)) if sum(t) == target])
  form = '-'.join(['{}']*darts)
  return [s for s in map(lambda s: form.format(*s), sets)]

