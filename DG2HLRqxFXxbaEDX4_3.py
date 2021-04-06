
def return_only_integer(lst):
  return [e for e in lst if str(e).isdigit() and isinstance(e, int)]

