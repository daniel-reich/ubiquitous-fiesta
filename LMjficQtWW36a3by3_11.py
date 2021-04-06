
def probability(lst, n):
  return round(len([i for i in lst if i >= n])/len(lst) * 100.0, 1)

