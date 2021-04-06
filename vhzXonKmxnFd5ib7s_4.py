
def matrix_multiply(a, b):
  if len(a[0]) != len(b):
    return "invalid"
  bT = list(zip(*b))
  return [[sum([x*y for x, y in zip(r, c)]) for c in bT] for r in a]

