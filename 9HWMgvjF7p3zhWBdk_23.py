
def keys_and_values(d):
  keys, vals = [], []
  for key, val in d.items():
    keys.append(key)    
  keys = sorted(keys)
  for key in keys:
    vals.append(d[key])
  return [keys, vals]

