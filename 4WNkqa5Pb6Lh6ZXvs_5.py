
def evaluate_polynomial(poly, x):
  valid = '1234567890+-^x()/'
  operators = '+-*/'
  if any([i not in valid for i in poly]) or '//' in poly or poly == '':
      return 'invalid'
  poly = poly.replace('^','**').replace('(','*(').replace('/','//')
  poly = list(poly)
  for i in range(len(poly)):
    if poly[i] == 'x':
      if i >= 1 and poly[i-1] not in operators and poly[i-1] != '(':
        poly[i] = '*x'
      elif i < len(poly)-1 and poly[i+1] == '(':
        poly[i] = 'x*'
  poly = ''.join(poly)
  return eval(poly)

