
def simple_equation(a, b, c):
  n1,n2,n3=0,0,0
  if a+b==c:
    n1,n2,n3=a,b,c
  elif a+c==b:
    n1,n2,n3=a,c,b
  elif b+c==a:
    n1,n2,n3=b,c,a
  if set([n1,n2,n3])==set([a,b,c]):
    return "{}+{}={}".format(n1,n2,n3)
  if a*b==c:
    n1,n2,n3=a,b,c
  elif a*c==b:
    n1,n2,n3=a,c,b
  elif b*c==a:
    n1,n2,n3=b,c,a
  if set([n1,n2,n3])==set([a,b,c]):
    return "{}*{}={}".format(n1,n2,n3)
  return ""

