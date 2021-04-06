
def is_legitimate(lst):
  return sum(lst[0])+sum(lst[-1])==0 and all(i[0]+i[-1]==0 for i in lst[1:-1])

