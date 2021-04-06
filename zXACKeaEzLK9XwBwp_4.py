
def split_bunches(bunches):
  lst = []
  for bunch in bunches:
    for i in range(0,bunch["quantity"]):
      lst.append(bunch)
  for bunch in lst:
    bunch["quantity"] = 1
  return lst

