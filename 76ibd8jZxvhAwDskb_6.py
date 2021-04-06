
def tallest_skyscraper(lst):
  bh=[]
  for a in range(len(lst[0])):
    h=0
    for b in range(len(lst)-1,-1,-1):
      if lst[b][a]!=0:
        h+=1
    bh.append(h)
  return max(bh)

