
def count_datatypes(*args):
  types = [int, str, bool, list, tuple, dict]
  if not args:
    return [0] * len(types)
​
  result = []
  for t in types:
    result.append(len([i for i in args if type(i) == t]))
  return result

