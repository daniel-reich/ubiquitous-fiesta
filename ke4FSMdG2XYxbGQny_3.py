
def even_odd_transform(lst, n):
  c=[]
  for i in lst:
    if i%2==0:
      c.append(i-2*n)
    else:
      c.append(i+2*n)
  return c

