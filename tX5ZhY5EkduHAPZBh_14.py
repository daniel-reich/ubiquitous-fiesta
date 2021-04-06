
def nearest_element(n, lst):
  ds = sorted(lst, key = lambda x: abs(x-n-0.1))
  return lst.index(ds[0])

