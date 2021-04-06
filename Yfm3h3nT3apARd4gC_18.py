
def rolls(lst):
  for x in range(len(lst[1:])-1,-1,-1,):
    if lst[x]==1:
      lst[x+1]=0
    if lst[x]==6:
      lst[x+1]=lst[x+1]*2
  return (sum(lst))

