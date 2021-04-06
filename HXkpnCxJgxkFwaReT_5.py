
def count_datatypes(*args):
  types = {int:0, str:0, bool:0, list:0, tuple:0, dict:0}
  for t in types:
    for arg in args:
      if type(arg) == t:
        types[t] += 1
  return [types[int], types[str], types[bool], types[list], types[tuple], types[dict]]

