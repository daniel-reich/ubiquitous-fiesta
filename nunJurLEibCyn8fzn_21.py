
def filter_list(lst):
  newList = []
  for i in lst:
    if isinstance(i, int):
      newList.append(i)
  return newList

