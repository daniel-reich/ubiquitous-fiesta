
def split_bunches(bunches):
  temp_bunches = []
  for dicts in bunches:
      for num in range(dicts["quantity"]):
          temp_bunches.append({"name":dicts["name"], "quantity" : 1})
  return temp_bunches

