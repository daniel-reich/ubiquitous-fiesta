
def probability(lst, n):
  count = 0
  for i in lst:
    if i >= n:
      count += 1
  return round(count / len(lst) * 100, 1)

