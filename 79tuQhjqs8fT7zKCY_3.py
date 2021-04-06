
def postfix(expr):
  l=[]
  for i in expr.split():
    if i.isdigit():l.append(i)
    else:
      b,a=l.pop(),l.pop()
      l.append(str(eval(a+i+b)))
  return int(float(l.pop()))

