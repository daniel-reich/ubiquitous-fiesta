
def split_bunches(bunches):
  s = []
  for bunch in bunches:
    for i in range(bunch["quantity"]):
      s.append({"name" : bunch["name"], "quantity" : 1})
  return s

