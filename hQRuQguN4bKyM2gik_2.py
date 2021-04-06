
def simple_check(a, b):
  seq = zip(range(a,0,-1), range(b, 0, -1))
  return sum(1 for c, d in seq if not (max(c,d) % min(c,d)))

