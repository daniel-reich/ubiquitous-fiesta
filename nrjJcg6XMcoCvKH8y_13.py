
def validate_subsets(subsets, my_set):
  for x in subsets:
    if not set(x)<=set(my_set): return False
  return True

