
def cycle_length(l, n):
  goal = sorted(l)
  i = 0
  while l[goal.index(n)] != n:
    q = l.index(n)
    l[q], l[goal.index(n)] = l[goal.index(n)], l[q]
    n = l[q]
    i += 1
  return i

