
def get_type(value):
  if isinstance(value, bool):
    return "bool"
  elif isinstance(value, str):
    return "str"
  elif isinstance(value, int):
    return "int"
  elif isinstance(value, list):
    return "list"
  elif isinstance(value, set):
    return "set"
  elif isinstance(value, tuple):
    return "tuple"
  elif isinstance(value, dict):
    return "dict"
  else:
    return "NoneType"

