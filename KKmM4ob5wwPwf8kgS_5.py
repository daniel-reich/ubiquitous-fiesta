
def get_frequencies(lst):
  d = {}
  for i in lst:
    if i not in d:
      d[i] = 0
    d[i] += 1
  return d

