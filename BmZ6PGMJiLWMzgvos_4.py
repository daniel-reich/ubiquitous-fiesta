
def is_special_array(lst):
  return all(i % 2 == j % 2 for i, j in enumerate(lst))

