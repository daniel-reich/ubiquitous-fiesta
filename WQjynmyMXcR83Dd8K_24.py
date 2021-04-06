
def number_of_swaps(lst):
  sortlst=lst
  testlist=sorted(lst)
  count=0
  while sortlst!=testlist:
    for i in range(len(sortlst)-1):
      if sortlst[i]>sortlst[i+1]:
        sortlst[i],sortlst[i+1] = sortlst[i+1],sortlst[i]
        count+=1
    print (sortlst)
  return count

