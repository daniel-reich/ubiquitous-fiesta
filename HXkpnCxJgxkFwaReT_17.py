
def count_datatypes(*args):
  data_types = [int, str, bool, list, tuple, dict]
  input_types = [type(arg) for arg in args]
  return [input_types.count(dt) for dt in data_types]

