
def where_is_waldo(lst):
  for i in range(0, len(lst)):
    for j in range(0, len(lst[i])):
      if lst[i][j]!=lst[0][0]:
        return [i+1,j+1]

