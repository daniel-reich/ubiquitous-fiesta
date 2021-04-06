
def nearest_element(n, lst):
  i = min(sorted(lst, reverse=True), key=lambda x: abs(x-n))
  return lst.index(i)

