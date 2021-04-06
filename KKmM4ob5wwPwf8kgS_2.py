
def get_frequencies(lst):
  d = {}
  for i in set(lst):
    d[i] = lst.count(i)
  return d

