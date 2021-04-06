
def find_and_remove(dct):
  out = dict()
  for k, v in dct.items():
    if isinstance(v, dict):
      out[k] = find_and_remove(v)
    elif v.isnumeric():
      out[k] = int(v)
  return out

