
def matrix(x, y, z):
  lst = []
  lst2 = []
  for i in range (0,x):
    lst2 = []
    for h in range (0,y):
      lst2.append(z)
    lst = lst + [lst2]
  return lst

