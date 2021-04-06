
def nearest_element(n, lst):
  return lst.index(sorted(sorted(lst)[::-1], key=lambda x: abs(n-x))[0])

