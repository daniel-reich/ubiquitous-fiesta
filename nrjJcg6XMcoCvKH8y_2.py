
def validate_subsets(subsets, my_set):
  return all([x in my_set for y in subsets for x in y])

