
def count_repetitions(lst):
  arr = [[lst.count(x), x] for x in set(lst)]
  d = dict()
  for y in sorted(arr)[::-1]:
    d[y[1]] = y[0]
  return d

