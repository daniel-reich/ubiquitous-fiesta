
def is_shifted(lst1, lst2):
  return len(set(j - i for i, j in zip(lst1, lst2))) == 1
​
def is_multiplied(lst1, lst2):
  return len(set(j / i for i, j in zip(lst1, lst2))) == 1

