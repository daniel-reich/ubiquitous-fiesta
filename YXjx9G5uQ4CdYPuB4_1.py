
def simple_comp(l1, l2):
  if None in (l1, l2):
    return False
​
  return sorted(map(lambda x: x ** 2, l1)) == sorted(l2)

