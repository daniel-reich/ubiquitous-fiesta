
def validate_subsets(subsets, my_set):
  for x in subsets:
    for y in x:
      if y not in my_set:
        return False
  return True

