
def hex_lattice(n):
  r = (3 + (12 * n - 3)**0.5) / 6
  layers = int(r)
  if layers != r : return "Invalid"
  rlen = layers*4 -1
  prnt = []
  d = (layers-1)*2
  for _ in range(layers):
    prnt.append('{: ^{}}'.format('o '*d + 'o', rlen))
    d -= 1
  return '\n'.join(prnt[1:][::-1] + prnt)

