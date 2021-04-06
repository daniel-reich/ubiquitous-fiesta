
def keys_and_values(d):
  return [sorted(list(d.keys())), [d.get(value) for value in sorted(list(d.keys()))]]

