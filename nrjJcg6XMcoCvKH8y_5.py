
def validate_subsets(subsets, my_set):
  return all([set(subset) <= set(my_set) for subset in subsets])

