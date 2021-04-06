
def check(lst):
  x,y,z = ("increasing","decreasing","neither")
  if len(lst) != len(set(lst)):
    return z
  for i in range(len(lst)-1):
    if lst[i+1] > lst[i]:
      return x
    elif lst[i+1] < lst[i]:
      return y

