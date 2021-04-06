
def meet_sum(prev, idx, sections, darts, target, possible):
    s = sum(prev)
    if s == target and len(prev) == darts:
        possible.append(tuple(prev))
        return None
    if len(prev) > darts or s > target:
        return None
    for idx2 in range(idx, len(sections)):
        meet_sum(
          prev + [sections[idx2]],
          idx2,
          sections,
          darts,
          target,
          possible,
        )
​
def darts_solver(sections, darts, target):
  poss = []
  meet_sum([], 0, sections, darts, target, poss)
  return ['-'.join([repr(x) for x in p]) for p in sorted(poss)]

