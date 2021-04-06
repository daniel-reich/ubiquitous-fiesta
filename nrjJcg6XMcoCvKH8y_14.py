
def validate_subsets(subsets, my_set):
  return all(set(s) <= set(my_set) for s in subsets)

