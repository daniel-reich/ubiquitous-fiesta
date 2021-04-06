
def is_special_array(lst):
  return all(i%2 == v%2 for i, v in enumerate(lst))

