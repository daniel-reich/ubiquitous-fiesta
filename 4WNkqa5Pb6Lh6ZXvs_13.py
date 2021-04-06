
def evaluate_polynomial(poly, num):
  acceptable = '0123456789+-^*/x()'
  if not poly or '//' in poly or any(ch not in acceptable for ch in poly):
    return "invalid"
​
  x = num
  poly = poly.replace('(','*(').replace('^','**')
  for i in range(10):
    if str(i)+'x' in poly:
      poly = poly.replace(str(i)+'x',str(i)+'*x')
  return eval(poly)

