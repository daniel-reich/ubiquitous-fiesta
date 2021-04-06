
def multiply_matrix(m1, m2):
  if len(m1)!=len(m2[0]):
    return "ERROR"
  return [[sum(a*b for a,b in zip(x,y)) for y in zip(*m2)] for x in m1]

