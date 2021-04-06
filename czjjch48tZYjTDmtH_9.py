
def is_shifted(lst1, lst2):
  diff = [y-x for x, y in zip(lst1, lst2)]
  return len(set(diff)) == 1
​
def is_multiplied(lst1, lst2):
  if all(x == 0 for x in lst1) or all(x == 0 for x in lst2):
    return True
  mul = [y / x for x, y in zip(lst1, lst2)]
  return len(set(mul)) == 1

