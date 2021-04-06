
def probability(lst, n):
  return round(sum(1 for x in lst if x >= n) / len(lst) * 100, 1)

