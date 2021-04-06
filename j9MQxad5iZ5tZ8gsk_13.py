
def find_vertex(x):
  a,b = [int(i[:-1]) for i in x.split() if 'x' in i]
  return -b//(2*a)

