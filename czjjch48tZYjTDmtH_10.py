
def is_shifted(lst1, lst2):
  new = list( y-x for x, y in zip(lst1, lst2))
  return len(set(new)) == 1
  
​
def is_multiplied(lst1, lst2):
  new = list( y/x for x, y in zip(lst1, lst2))
  return len(set(new)) == 1

