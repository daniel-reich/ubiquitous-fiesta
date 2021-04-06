
def make_box(n):
  a=n
  x=''
  fin=''
  y=[]
  for i in range(a):
    x+='#'
  for i in range(a):
    y.append(x)
  for i in range(len(y)):
    if i!=0 and i!=len(y)-1:
      y[i]=y[i].replace('#',' ')
  for i in range(len(y)):
    if '#' not in y[i]:
      y[i]=y[i][2:]+y[i][:len(y)-a]
      y[i]='#'+y[i]+'#'
  return(y)

