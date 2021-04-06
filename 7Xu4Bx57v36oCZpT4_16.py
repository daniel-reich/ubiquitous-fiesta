
def where_is_waldo(lst):
  elem = elem = lst[0][0]
  for i in range(len(lst)):
    for j in range(len(lst[i])):
      if lst[i][j] != elem:
        return [i+1,j+1]

