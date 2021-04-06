
def get_frequencies(lst):
  st= set(lst)
  return dict(zip(st,[lst.count(x) for x in st]))

