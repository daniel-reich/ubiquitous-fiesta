
def rep_set(n):
  return [] if not n else rep_set(n-1) + [rep_set(n-1)]

