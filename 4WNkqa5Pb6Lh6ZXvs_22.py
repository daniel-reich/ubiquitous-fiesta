
def evaluate_polynomial(poly, num):
  tmp=poly.replace('//','-*--').replace('(','*(').replace('(*(','((')
  for i in range(10):
    tmp=tmp.replace(str(i)+'x',str(i)+'*x')
  tmp=tmp.replace('x',str(num)).replace('^','**')
  try:
    out=eval(tmp)
  except:
    return "invalid"
  return out

