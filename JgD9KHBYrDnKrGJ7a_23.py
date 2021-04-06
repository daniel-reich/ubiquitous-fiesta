
def swap_dict(dic):
  d = {}
  for k, v in dic.items():
    d.setdefault(v, []).append(k)
  return d

