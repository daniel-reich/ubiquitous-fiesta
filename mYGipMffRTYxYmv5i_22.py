
def simple_equation(a, b, c):
  a,b,c, = sorted([a,b,c])
  
  if a + b == c:
    return '{}+{}={}'.format(a,b,c)
  if a * b == c:
    return '{}*{}={}'.format(a,b,c)
  
  return ''

