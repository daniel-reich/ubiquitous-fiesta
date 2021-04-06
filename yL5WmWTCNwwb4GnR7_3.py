
def return_unique(lst):
  return list(filter(lambda x: lst.count(x) < 2, lst))

