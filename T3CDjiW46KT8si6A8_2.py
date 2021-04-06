
def product(l):
  l = sorted(set(l))
  return l[-2]*l[-1] if len(l) > 1 else l[0]**2

