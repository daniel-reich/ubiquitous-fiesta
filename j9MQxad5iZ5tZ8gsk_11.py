
def find_vertex(x):
  v = []
  elems = x.split()
  for elem in elems:
    if elem[-1] == 'x':
      v.append(int(elem[:-1]))
  return -v[1] // (2 * v[0])

