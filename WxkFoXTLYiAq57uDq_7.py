
def find_and_remove(dct):
  new_dict = {}
  for key, subdict in dct.items():
    new_dict[key] = {}
    for item, value in subdict.items():
      if not value.isdigit():
        continue
      new_dict[key][item] = int(value)
  return new_dict

