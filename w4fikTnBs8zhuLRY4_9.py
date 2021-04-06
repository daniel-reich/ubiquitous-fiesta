
def rep_set(n):
  if n == 0:
    return []
  else:
    return rep_set(n-1) + [rep_set(n-1)]

