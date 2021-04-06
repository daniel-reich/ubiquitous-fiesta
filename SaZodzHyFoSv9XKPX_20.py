
def domino_chain(dominos):
  x = dominos.split(' ')
  y = x[0].split('/')
  y[0] = '/'*len(y[0])
  y = '/'.join(i for i in y)
  print(y)
  x[0] = y
  return ' '.join(i for i in x)

