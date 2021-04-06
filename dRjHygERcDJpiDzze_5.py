
def lengthen(s1, s2):
  a=s1
  b=s2
  if len(a)>len(b):
    x=a
    y=b
  else:
    x=b
    y=a
  for i in x:
    for j in y:
      if len(x)!=len(y):
        y+=j
  return(y)

