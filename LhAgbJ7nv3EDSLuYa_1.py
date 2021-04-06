
def golomb(n):
  l=[0,1]
  for i in range(1,n):l.append(1+l[i+1-l[l[i]]])
  return l[1:]

