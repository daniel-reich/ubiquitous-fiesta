
def every_some(test, val, a, b, c, d, e):
  if val == 'everybody':
    return all(eval('{} '.format(i)+test) for i in [a,b,c,d,e])
  else:
    return any(eval('{} '.format(i)+test) for i in [a,b,c,d,e])

