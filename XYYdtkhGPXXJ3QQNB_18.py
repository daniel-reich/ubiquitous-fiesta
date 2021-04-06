
def num_in_str(lst):
  return [s for s in lst if (True in [l.isdigit() for l in s])]

