
def ordered_matrix(a, b):
  m=[]
  x=0
  for i in range(a):
    m.append([])
    for j in range(1,b+1):
      m[i].append(x+1)
      x=x+1
  return m

