
def nearest_element(n, lst):
  return lst.index(min(sorted(lst,reverse=True), key=lambda x:abs(x-n)))

