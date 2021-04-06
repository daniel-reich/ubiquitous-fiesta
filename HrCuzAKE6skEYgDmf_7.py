
def pairs(dizi):
  arr=[]
  j=-1
  c=0
  if len(dizi)%2==0:
    c=0
  else:
    c=1
  for i in range(len(dizi)//2+c):
    arr.append([dizi[i],dizi[j]])
    j=j-1
  return arr

