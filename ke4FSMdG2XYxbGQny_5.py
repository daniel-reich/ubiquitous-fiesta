
def even_odd_transform(lst, n):
  l=lst
  if len(l)==0:
    return l
  for i in range(n):
    for j in range(len(l)):
      if l[j]%2==0:
        l[j]=l[j]-2
      else:
        l[j]=l[j]+2
  return l

