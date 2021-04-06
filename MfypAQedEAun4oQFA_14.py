
def perrin(n):
  L=[3,0,2]
  for i in range(2,n):
    L.append(L[i-2]+L[i-1])
    i+=1
  return L[n]

