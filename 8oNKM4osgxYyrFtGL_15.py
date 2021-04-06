
def multiply(l):
  lst = []
  for i in range(len(l)):
    tmp = []
    for j in range(len(l)):
      tmp.append(l[i])
    lst.append(tmp)
  return lst

