
def multiply_matrix(m1, m2):
  if len(m1[0]) != len(m2): return "ERROR"
  return [[sum(a*b for a, b in zip(r1,c2)) for c2 in zip(*m2)] for r1 in m1]

