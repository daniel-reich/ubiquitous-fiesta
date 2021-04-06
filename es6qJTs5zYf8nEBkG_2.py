
def dup(n):
  for i,j in enumerate(n):
    for k,l in enumerate(n):
      if i!=k:
        if j==l:
          return True
  return False
def is_rectangle(coordinates):
  l=[]
  for i in coordinates:
    x=i.split(',')
    x[0]=int(x[0][1:])
    x[1]=int(x[1][:-1])
    l.append(x)
  if len(l)!=4:
    return False
  x1,x2,y1,y2=0,0,0,0
  for n1,i in enumerate(l):
    for n2,j in enumerate(l):
      if n1!=n2 and not dup(l):
        if i[0]==j[0]:
          if x1==0:
            x1=1
          else:
            x2=1
        if i[1]==j[1]:
          if y1==0:
            y1=1
          else:
            y2=1
  if x1 and x2 and y1 and y2:
    return True
  return False

