
def tallest_skyscraper(lst):
  towers = {}
  for i in lst:
    for ind,k in enumerate(i):
      towers[ind] = 0
  for i in lst:
    for ind,k in enumerate(i):
      if k == 1:
        towers[ind] += 1
      else:
        towers[ind] += 0
  return max(i for i in towers.values())

