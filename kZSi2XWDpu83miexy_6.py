
def post_fix(expr): 
  expr = expr.split()
  d,f = [i for i in expr if i.isdigit()],[i for i in expr if not i.isdigit()]
  for i in range(1,len(d)):
    d[i] = str(eval(d[i-1]+f[0]+d[i]))
    f = f[1:]
  return float(d[-1])

