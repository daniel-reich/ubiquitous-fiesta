
def count_datatypes(*args):
  return [sum((lambda x: type(x) == t) (i) for i in args) for t in [int, str, bool, list, tuple, dict]]

