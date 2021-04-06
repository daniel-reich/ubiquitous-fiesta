
def block(lst):
  x = 0
  for i in range(0, len(lst)-1):
    for j in lst[i]:
      if j == 2:
        x+= len(lst)-1-i
  return x

