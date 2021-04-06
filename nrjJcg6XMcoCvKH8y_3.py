
def validate_subsets(subsets, my_set):
  return all([set(s).issubset(my_set) for s in subsets])

