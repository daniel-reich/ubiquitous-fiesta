
def num_of_sublists(lst):
  return sum(1 for x in lst if isinstance(x, list))

