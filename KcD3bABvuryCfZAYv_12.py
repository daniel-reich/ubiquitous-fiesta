
def most_frequent_char(lst):
  d = {}
  for i in lst:
    for j in i:
      if j in d:
        d[j] += 1
      else:
        d[j] = 1
  return sorted([key for m in [max(d.values())] for key,val in d.items() if val == m])

