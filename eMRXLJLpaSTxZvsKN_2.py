
def is_ladder_safe(ldr):
  n = len(ldr[0])
  if n >= 5:
    rung = '#'*n
    not_rung = '#' + ' '*(n-2) + '#'
    if all(row in [rung,not_rung] for row in ldr):
      rungs = [i for i in range(len(ldr)) if ldr[i] == rung]
      gap = [b-a for a, b in zip(rungs,rungs[1:])]
      return len(set(gap)) == 1 and gap[0] <= 3
  return False

