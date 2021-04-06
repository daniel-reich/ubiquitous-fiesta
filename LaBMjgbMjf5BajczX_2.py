
def count_layers(a):
  m=len(a)//2
  c=1
  for i in range(m):
    if a[i]!=a[i+1]:
      c+=1
    if len(a[m])//2==i:
      return c
  return c

