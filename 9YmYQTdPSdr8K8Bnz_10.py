
def unique_lst(lst):
  r = []
  [r.append(i) for i in lst if i > 0 and i not in r]
  return r

