
def is_legitimate(lst):
  firstrow, *mid, lastrow = lst
  updwn = any(firstrow) == any(lastrow) == 0
  leftright = all(row[0] == row[-1] == 0 for row in mid)
  return updwn and leftright

