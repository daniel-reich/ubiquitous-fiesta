
def return_only_integer(lst):
  return [i for i in lst if isinstance(i, int) and not isinstance(i, bool)]

