
def probability(lst, n):
  return round(sum(i >= n for i in lst) / len(lst) * 100, 1)

