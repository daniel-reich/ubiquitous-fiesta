
def rep_set(n):
  if not n:
    return []
  else:
    return [rep_set(i) for i in range(n)]

