
def is_shifted(lst1, lst2):
  return len(set(b - a for a, b in zip(lst1, lst2))) == 1
​
def is_multiplied(lst1, lst2):
  return all(e == 0 for e in lst2) or len(set(b / a for a, b in zip(lst1, lst2))) == 1

