
def is_shifted(lst1, lst2):
  diff = lst2[0] - lst1[0]
  for i in range(len(lst1)):
    if lst2[i] != lst1[i] + diff:
      return False
  return True
def is_multiplied(lst1, lst2):
  m = lst2[0]/lst1[0]
  for i in range(len(lst1)):
    if lst2[i] != lst1[i]*m:
      return False
  return True

