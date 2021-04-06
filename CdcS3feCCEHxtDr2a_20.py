
def clear_ordering(lst):
  for i in range(len(lst)):
    for x in range(i+1,len(lst)):
      if lst[i][0]==lst[x][0] or lst[i][1]==lst[x][1]: return False
  return True

