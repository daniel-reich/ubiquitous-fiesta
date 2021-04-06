
def count_repetitions(lst):
  d={}
  for x in set(lst):
    d[x]=lst.count(x)
  return d

