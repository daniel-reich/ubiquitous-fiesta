
def is_special_array(lst):
  return all(i % 2 == e % 2 for i, e in enumerate(lst))

