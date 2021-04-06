
def filter_list(lst):
  res = []
  [res.append(x) for x in lst if type(x) is not str]
  return res

