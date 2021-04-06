
def return_only_integer(lst):
  lst1 = []
  for x in lst:
    if type(x) == int:
      lst1.append(x)
  return lst1

