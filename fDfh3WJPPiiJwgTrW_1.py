
def num_of_sublists(lst):
  return sum(isinstance(i, list) for i in lst)

