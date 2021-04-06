
def discount(n, txt):
  if not txt: return n
  d = [float(x.replace("%",''))/100 if '%' in x and x else float(x) if x else False for x in txt.split(',')]
  d.sort()
  for x in d:
    if x>=1:  n-=x
    else: n-=(n*x)
  return round(n,2)

