
def num_of_sublists(lst):
  return sum([str(type(i)) == "<class 'list'>" for i in lst])

