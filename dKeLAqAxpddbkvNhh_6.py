
def group_seats(lst, n):
  options = 0
  for row in lst:
    row_free = 0
    for seat in row:
      if seat==0:
        row_free+=1
      else:
        row_free = 0
      if row_free>=n:
        options+=1
  return options

