
def validate_subsets(subsets, my_set):
  for sub in subsets:
    for num in sub:
      if num not in my_set:
        return False
        break
  return True

