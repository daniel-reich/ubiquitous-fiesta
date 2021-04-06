
def rep_set(n):
  return [] if n==0 else rep_set(n-1)+[rep_set(n-1)]

