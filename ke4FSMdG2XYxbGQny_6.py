
def even_odd_transform(lst, n):
  i=n
  new=[]
  for x in lst:
    if x%2:
      new.append(x+2*n)
    if not x%2:
      new.append(x-2*n)
  return new

