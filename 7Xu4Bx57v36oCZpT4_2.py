
def where_is_waldo(lst):
  for i in range(len(lst)):
    for j in range(len(lst[i])):
      if lst[i].count(lst[i][j]) == 1:
        return [lst.index(lst[i]) + 1, lst[i].index(lst[i][j]) + 1]

