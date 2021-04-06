
def probability(lst, n):
  gcount = 0
  for i in lst:
    if i >= n:
      gcount += 1
  return round(gcount/len(lst) * 100, 1)

