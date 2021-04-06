
def simple_pair(lst, n):
  for x in lst:
   lst.pop(lst.index(x))
   for y in lst:
     if x*y==n:
       return sorted([x,y])
  return None

