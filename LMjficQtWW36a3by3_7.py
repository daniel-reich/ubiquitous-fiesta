
def probability(lst, n):
  c = 0
  for i in lst:
    if i >= n:
      c += 1
  return round((c/len(lst))*100,1)

