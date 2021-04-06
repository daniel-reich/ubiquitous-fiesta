
def keys_and_values(d):
  sorted_keys = list(d.keys())
  sorted_keys.sort()
  values = [d[key] for key in sorted_keys]
  return [sorted_keys, values]

