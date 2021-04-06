
def rep_set(n):
  return [rep_set(i) for i in range(n)] if n else []

