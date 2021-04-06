
def list_values_types(lst):
  return [str(type(x)).split(' ')[1][1:-2] for x in lst]

