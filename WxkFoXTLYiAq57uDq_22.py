
def find_and_remove(dct):
  for key,value in dct.items():
    if isinstance(value,dict):
      dct[key] = find_and_remove(value)
    elif value.isdigit():
      dct[key] = int(value)
    else:
      dct[key] = None
  return {x: dct[x] for x in dct.keys() if dct[x] is not None}

