
def where_is_waldo(lst):
  row=0
  col=0
  for i in range(len(lst)):
    row+=1
    for j in range(len(lst[i])):
      col+=1
      if lst[i].count(lst[i][j])==1:
        return [row,col]
    col=0

