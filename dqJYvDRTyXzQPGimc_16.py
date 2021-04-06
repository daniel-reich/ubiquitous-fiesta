
def is_unfair_hurdle(a):
  return len(a) >= 4 or a[0].count(' ') / (a[0].count('#')-1) < 4

