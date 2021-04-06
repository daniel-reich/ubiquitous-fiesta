
def min_removals(txt1, txt2):
  x=list(txt1)
  y=list(txt2)
  y.sort()
  d="".join(y)
  e="".join(x)
  z=[]
  for i in range(len(x)):
      if x[i] in y:
          z.append(x[i])
  a=("".join(z))
  b=d.strip(a)
  c=e.strip(a)
  return(len(b)+len(c))

