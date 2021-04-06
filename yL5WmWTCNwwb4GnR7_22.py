
def return_unique(lst):
  uniques = []
  for el in lst:
    count = lst.count(el)
    if count == 1:
      uniques.append(el)
  return uniques

