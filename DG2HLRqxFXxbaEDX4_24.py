
def return_only_integer(lst):
  nylst = []
  for i in lst:
    if type(i) == int:
      nylst.append(i)
  return nylst

