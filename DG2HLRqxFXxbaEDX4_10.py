
def return_only_integer(lst):
  for x in lst:
    if not type(x) == int:
      lst.remove(x)
  for x in lst:
    if not type(x) == int:
      lst.remove(x)
  return lst

