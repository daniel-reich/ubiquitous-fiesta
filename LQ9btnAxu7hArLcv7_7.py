
def diagonalize(n, d):
  x = range(n)
  y = []
  for i in x:
    y.append(list(range(i,i+n)))
  if d[0] == 'l':
    y.reverse()
  if d[1] == 'r':
    for i in y:
      i.reverse()
  return y

