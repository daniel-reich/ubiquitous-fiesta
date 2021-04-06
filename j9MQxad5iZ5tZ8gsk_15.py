
def find_vertex(x):
  b = ''
  for a in x:
    if a != ' ':
      b += a
  b = b.split('x')
  return -int(b[1]) // (2 * int(b[0]))

