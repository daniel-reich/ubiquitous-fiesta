
def direction(lst):
  for i in range(len(lst)):
    lst[i] = lst[i].replace('e','w').replace('E','W').replace('a','e').replace('A','E')
  return lst

