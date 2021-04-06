
def diamond_arrays(x):
  lst = []
  for i in range(1,x+1):
    lst.append([i]*i)
  for i in range(x-1,0,-1):
    lst.append([i]*i)
  return lst

