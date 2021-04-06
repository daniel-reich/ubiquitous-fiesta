
def validate_subsets(subsets, my_set):
  return all(set(sub).issubset(set(my_set)) for sub in subsets)

