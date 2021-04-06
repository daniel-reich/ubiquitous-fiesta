
def leader(a):
  return [x for idx,x in enumerate(a) if x >= max(a[idx:])]

