
def disjoint_cycle_form(perm):
  ordered = sorted(perm)
  permmap = dict(zip(ordered, perm))
  cycles = set()
  while ordered:
    a = ordered[0]
    cycle = []
    while True:
      cycle.append(a)
      ordered.remove(a)
      b = permmap[a]
      if b in cycle:
        break
      a = b
    if len(cycle) > 1:
      cycles.add(normalize_cycle(cycle))
  return cycles
​
​
def normalize_cycle(cycle):
  m = min(cycle)
  while cycle[0] > m:
    cycle = cycle[1:] + (cycle[0],)
  return tuple(cycle)

