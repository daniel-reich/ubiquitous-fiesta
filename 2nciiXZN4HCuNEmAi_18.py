
def flatten(r):
  if all(not isinstance(item, list) for item in r):
    return r
  items = []
  for item in r:
    if not isinstance(item, list):
      items.append(item)
    else:
      for sub_item in item:
        items.append(sub_item)
  return flatten(items)

