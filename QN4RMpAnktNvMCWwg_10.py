
def id_mtrx(n):
  matrix=[]
  if(isinstance(n,str)):
    return "Error"
  if(n>0):
    x=-1
    for i in range(0,n):
      matrix.append([])
      x+=1
      y=0
      for j in range(0,n):
        if (x==y):
          matrix[i].append(1)
        else:
          matrix[i].append(0)
        y+=1
    return matrix
  if(n<0):
    x=abs(n)
    for i in range(0,abs(n)):
      matrix.append([])
      x-=1
      y=0
      for j in range(0,abs(n)):
        if (x==y):
          matrix[i].append(1)
        else:
          matrix[i].append(0)
        y+=1
    return matrix

