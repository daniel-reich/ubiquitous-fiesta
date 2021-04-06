
def split_bunches(bunches):
  return [el for sl in [[{"name" : f.get("name"), "quantity" : 1} for _ in range(f.get("quantity"))] for f in bunches] for el in sl]

