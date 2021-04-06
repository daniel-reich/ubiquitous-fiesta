
def probability(lst, n):
  fav = [x for x in lst if n <= x]
  return round(100*(len(fav)/len(lst)),1)

