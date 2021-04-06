
def probability(lst, n):
  return round(100*sum(i>= n for i in lst)/len(lst),1)

