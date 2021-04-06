
def num_in_str(lst):
  return [x for x in lst if any(i.isdigit() for i in x)]

