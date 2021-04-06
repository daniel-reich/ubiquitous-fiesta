
def validate_subsets(subsets, my_set):
  lst = []
  for x in subsets:
    lst += x
  return set(lst) == set(my_set)

