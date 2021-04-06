
def nearest_element(n, lst):
  closest = [el for el in lst if abs(n-el)==min(abs(n-x) for x in lst)]
  return lst.index(max(closest))

