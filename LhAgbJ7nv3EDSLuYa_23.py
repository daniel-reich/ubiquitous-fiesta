
def golomb(n):
  lst=[1,2,2]
  if(n<=2):
    return lst[0:n]
  else:
    i=2
    while(len(lst)<=n and i<n):
      j=i+1
      x=lst[i]
      lst.extend([j]*x)
      i+=1
    return lst[0:n]

