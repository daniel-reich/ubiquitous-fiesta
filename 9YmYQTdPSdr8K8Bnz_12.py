
def unique_lst(lst):
  x, a = list(filter(lambda y: y > 0, lst)), []
  for char in x:
    if char not in a:
      a.append(char)
  return a

