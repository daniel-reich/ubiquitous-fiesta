
def completely_filled(lst):
  for i in range(0,len(lst)):
    for j in range(0,len(lst[0])):
      if lst[i][j] == " ":
        return False
  return True

