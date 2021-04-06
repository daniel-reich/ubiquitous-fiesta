
def probability(lst, n):
​
  over = []
  under = []
  lst = sorted(lst)
  for i in lst:
    if i >= n:
      over.append(i)
    else:
      under.append(i)
  return round(100 * len(over) / len(lst), 1)

