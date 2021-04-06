
def get_length(lst):
  return 1 if type(lst) is int else sum(get_length(i) for i in lst)

