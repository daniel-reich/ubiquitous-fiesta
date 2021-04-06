
def num_of_sublists(lst):
  return sum(type(e)==list for e in lst)

