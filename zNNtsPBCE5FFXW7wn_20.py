
def empty_values(l):
  types = {
  int: 0,
  float: 0.0,
  str: "",
  bool: False,
  list: [],
  tuple: (),
  set: set(),
  type(None): None
  }
  return [types[type(i)] for i in l]

