
def prefix(e):
  s=[]
  for x in e.split():s.append(x if x in'+-*/'or s[-1]in'+-*/'else str(eval(s.pop()+s.pop().replace('/','//')+x)))
  while len(s)>1:
    e=s
    s=[]
    for x in e:s.append(x if x in'+-*/'or s[-1]in'+-*/'else str(eval(s.pop()+s.pop().replace('/','//')+x)))
  return int(s[0])

