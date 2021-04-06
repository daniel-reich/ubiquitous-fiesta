
def multiply_matrix(m1, m2):
  if len(m1[0]) != len(m2): return "ERROR"
  return [[sum(a*b for a,b in zip(i,j)) for j in zip(*m2)] for i in m1]

