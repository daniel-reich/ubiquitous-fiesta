
def probability(lst, n):
  return round((len([i for i in lst if i>=n])*100/len(lst)),1)

