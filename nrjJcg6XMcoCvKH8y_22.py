
def validate_subsets(subsets, my_set):
  for subset in subsets:
    for i in subset:
      if not i in my_set:
        return False
  return True

