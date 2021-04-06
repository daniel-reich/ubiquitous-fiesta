
def find_vertex(x):
  x = x.replace("+", " ")
  v = x.split()
  a = int(v[0][:-1])
  b = int(v[1][:-1])
  return -b // (2 * a)

