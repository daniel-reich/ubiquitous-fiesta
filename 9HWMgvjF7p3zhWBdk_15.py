
def keys_and_values(d):
  keys = []
  values = []
  for k, v in sorted(d.items()):
    keys.append(k)
    values.append(v)
  return [keys, values]

