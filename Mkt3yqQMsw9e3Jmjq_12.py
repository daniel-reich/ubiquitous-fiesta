
from itertools import dropwhile
def disjoint_cycle_form(perm):
  cycle = []
  right_place = lambda x: perm.index(x) == sorted(perm).index(x)
  while True:
    perm = list(dropwhile(lambda x: right_place(x),perm))
    if not perm:
      return set(cycle)
    cycle.append([min(perm),perm[0]])
    index = perm.index(min(perm))
    perm[index] = perm[0]
    perm.pop(0)
    index -= 1
    while True:
      if sorted(perm)[index] == perm[index]:
        cycle[-1] = tuple(cycle[-1])
        break
      index2 = sorted(perm).index(perm[index])
      cycle[-1].append(perm[index2])
      perm[index],perm[index2] = perm[index2],perm[index]

