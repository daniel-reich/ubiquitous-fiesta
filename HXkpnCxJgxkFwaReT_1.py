
def count_datatypes(*args):
  types = [int, str, bool, list, tuple, dict]
  return [sum(type(i) is t for i in args) for t in types]

