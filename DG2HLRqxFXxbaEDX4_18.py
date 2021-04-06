
def return_only_integer(lst):
  l = []
  for i in range(len(lst)):
    if type(lst[i]) == int:
      l.append(lst[i])
  return l

