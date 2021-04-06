
def is_shifted(lst1, lst2):
  d = [y-x for x,y in zip(lst1,lst2)]
  return all([d[0]==x for x in d])
​
def is_multiplied(lst1, lst2):
  d = [y/x for x,y in zip(lst1,lst2)]
  return all([d[0]==x for x in d])

