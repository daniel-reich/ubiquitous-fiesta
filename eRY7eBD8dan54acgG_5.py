
def is_checkerboard(lst):
  for i in range (len(lst)):
    for j in range (1,len(lst)):
      if lst[i][j]==lst[i][j-1]: return False
  
  for j in range (len(lst)):
    for i in range (1,len(lst)):
      if lst[i][j]==lst[i-1][j]: return False
  
  return True

