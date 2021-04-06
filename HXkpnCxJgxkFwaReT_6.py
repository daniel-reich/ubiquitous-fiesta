
def count_datatypes(*args):
  types = [int, str, bool, list, tuple, dict]
  result = []
  for i in types:
    result.append(list(map(type, args)).count(i))
  return result

