
def matrix_mult(m1, m2):
  return [[sum([x*y for x, y in zip(r, c)]) for c in list(zip(*m2))] for r in m1]

