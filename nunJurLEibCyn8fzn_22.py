
def filter_list(lst):
  newlst = []
  for element in lst:
    if type(element) == int:
      newlst.append(element)
  return newlst

