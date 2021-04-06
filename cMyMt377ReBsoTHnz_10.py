
def dict_to_list(d):
  new_list = []
  sorted_keys = list(d.keys())
  sorted_keys.sort()
  for k in sorted_keys:
    new_list.append((k,d[k]))
  return new_list

