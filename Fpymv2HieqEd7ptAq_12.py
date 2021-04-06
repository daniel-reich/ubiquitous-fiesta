
def split(txt):
  x=[0,0]
  y=[]
  for i in txt:
    if x[0] == x[1]:
      y.append(i)
    else:
      y[len(y)-1] += i
    if i == '(':
      x[0] +=1
    else:
      x[1] +=1
  return y

