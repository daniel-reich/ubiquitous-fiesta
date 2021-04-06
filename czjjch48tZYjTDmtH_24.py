
def is_shifted(lst1, lst2):
  diff = abs(lst1[0] - lst2[0])
  for i in range(len(lst1)):
    if (lst1[i] - lst2[i] == diff) or (lst1[i] + diff == lst2[i]):
      continue
    else:
      return False
  return True
​
def is_multiplied(lst1, lst2):
  multiplied_by = lst2[0] / lst1[0]
  for i in range(len(lst1)):
    if lst1[i] * multiplied_by == lst2[i]:
      continue
    else:
      return False
  return True

