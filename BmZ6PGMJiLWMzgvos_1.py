
def is_special_array(lst):
  return all([(i+v)%2 == 0 for i, v in enumerate(lst)])

