
def count_datatypes(*args):
  ls = [int, str, bool, list, tuple, dict]
  res = [0, 0, 0, 0, 0, 0]
  for i in args:
    res[ls.index(type(i))] += 1
  return res

