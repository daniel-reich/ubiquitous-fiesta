
def num_of_sublists(lst):
  return sum(isinstance(x,list) for x in lst)

