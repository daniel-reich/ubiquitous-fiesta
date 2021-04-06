
def keys_and_values(d):
  keys = []
  values = []
  for key in d.keys():
    keys.append(key)
  keys.sort()
  for key in keys:
    values.append(d[key])
  return [keys, values]

