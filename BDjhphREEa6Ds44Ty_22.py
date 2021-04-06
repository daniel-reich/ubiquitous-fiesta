
def bomb(lst):
  for i in range(3):
    lst[i][2]=round(lst[i][2]*0.343,3)
  A=[]
  for  i in range(3):
    B=[]
    for x in range(51):
      for y in range(51):
        if int(((lst[i][0]-x)**2+(lst[i][1]-y)**2)**.5)==int(lst[i][2]):
          B.append((x,y))
    A.append(B)
  res=set(A[0])
  for x in A:
    res&=set(x)
  return list(res)[-1]

