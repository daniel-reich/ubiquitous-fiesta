
def validate_subsets(subsets, my_set):
  return all(set(x).issubset(set(my_set)) for x in subsets)

