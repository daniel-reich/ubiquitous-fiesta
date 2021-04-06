
def evaluate_polynomial(poly, n):
  poly=list(poly.replace('x',str(n)).replace('^','**'))
  allowed = '01234567890()+-/*'
  if not poly or any(i not in allowed for i in poly): return 'invalid'
  for i in range(len(poly)-1):
    if (poly[i].isnumeric() and poly[i+1].isnumeric()) or poly[i].isnumeric() and poly[i+1]=='(':
      poly.insert(i+1,'*')
    if poly[i] in '+-/' and poly[i+1] in '+-/*': return 'invalid'
  return eval(''.join(poly))

