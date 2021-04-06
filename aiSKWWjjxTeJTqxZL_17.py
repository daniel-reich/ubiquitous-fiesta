
def complete_square(lst):
  row = len(lst)
  col = len(lst[0])
  while row<col:
    lst+=[[0]*col]
    row = len(lst)
  if row>col:
    for i in lst:
      i += [0]*(row-col)
  return lst

