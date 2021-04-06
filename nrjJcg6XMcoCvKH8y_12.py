
def validate_subsets(subsets, my_set):
  l = []
  for i in subsets:
    l.extend(i)
  return set(l) in set(my_set) or set(l) == set(my_set)

