
def keys_and_values(d):
  l1 = sorted(list(d.keys()))
  l2 = []
  for i in l1:
    l2.append(d[i])
  return [l1, l2]

