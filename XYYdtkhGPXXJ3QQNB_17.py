
def num_in_str(lst):
  return [x for x in lst if any(char.isdigit() for char in x)]

