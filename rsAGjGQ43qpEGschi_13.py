
def newton_raphson(c):
  x=0
  cp=[c[i]*(3-i) for i in range(len(c))]
  for i in range(20):
    cx=[c[i]*(x)**(3-i) for i in range(len(c))]
    cpx=[cp[i]*(x)**(2-i) for i in range(len(c)-1)]
    y=x-sum(cx)/sum(cpx)
    x=y 
  return round(x,3)

