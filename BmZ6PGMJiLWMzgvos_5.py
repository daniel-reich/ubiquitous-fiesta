
def is_special_array(lst):
  return all(i % 2 == item % 2 for i, item in enumerate(lst))

