
def find_odd(lst):
  uniques = []
  for x in lst:
    if uniques.count(x) == 0:
      uniques.append(x)
  for x in uniques:
    if lst.count(x) % 2 == 1:
      return x

