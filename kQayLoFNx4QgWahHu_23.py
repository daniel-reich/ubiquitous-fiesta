
def order(lst):
  A=[(i, x) for i, x in enumerate(lst)]
  return [x[0] for x in sorted(A, key=lambda k: k[1])]

