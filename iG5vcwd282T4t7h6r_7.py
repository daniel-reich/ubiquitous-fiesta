
def str_to_dict(lst):
  d = {}
  for sec in lst:
    x = sec.split('=')
    d[x[0]] = x[1]
  return d

