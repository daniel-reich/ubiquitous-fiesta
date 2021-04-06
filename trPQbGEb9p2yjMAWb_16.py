
def every_some(test, val, a, b, c, d, e):
  d = {'somebody': any(eval('i{}'.format(test)) for i in [a, b, c, d, e]), 'everybody': all(eval('i{}'.format(test)) for i in [a, b, c, d, e])}
  return d[val]

