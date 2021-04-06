
def multiply_matrix(m1, m2):
  if len(m1[0]) != len(m2): return "ERROR"
  m2 = list(zip(*m2))
  return [[sum(map(lambda z: z[0] * z[1], zip(x,y))) for y in m2] for x in m1]

