
def dict_to_list(d):
  keys,values = list(d.keys()),list(d.values())
  keys = sorted(keys)
  return [(keys[i],d[keys[i]]) for i in range(len(d))]

