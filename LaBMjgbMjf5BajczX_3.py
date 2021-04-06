
def count_layers(r):
  m=len(r)//2
  c=1
  for i in range(m):
    if r[i]!=r[i+1]:
      c += 1
    if len(r[m])//2==i:
      return c
  return c

