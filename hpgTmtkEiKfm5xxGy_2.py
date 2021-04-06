
def paths(x, y):
 if x==0 or y==0:
   return 1
 else:
  return paths(x-1, y)+paths(x, y-1)

