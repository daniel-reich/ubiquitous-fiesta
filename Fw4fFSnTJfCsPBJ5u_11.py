
def how_many_missing(lst):
  if lst==[]:
    return 0
  return len(range(lst[0],lst[-1]+1))-len(lst)

