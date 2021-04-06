
def nearest_element(n, lst):
  nearest = min([abs(i-n) for i in lst])
  return lst.index(max([i for i in lst if abs(i-n) == nearest]))

