
def probability(lst, n):
  return round((len([x for x in lst if x>=n]) / len(lst)) * 100, 1)

