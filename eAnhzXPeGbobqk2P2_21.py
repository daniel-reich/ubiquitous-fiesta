
def century(y):
  t, h = map(int, [str(y)[0:2], str(y)[2:]])
  c = str(t+1 if h else t)
  return '{} century'.format(c+'st' if c == '21' else c+'th')

