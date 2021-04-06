
def pyramid_lists(n):
 lst = []
 for x in range (1, n+1):
  lst.append(x * [str(x)])
 for z in lst:
  for i, y in enumerate(z):
   z[i] = int(y)
 return lst

