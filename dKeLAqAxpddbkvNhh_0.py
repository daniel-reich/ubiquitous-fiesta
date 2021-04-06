
def group_seats(lst, n):
  spots = 0
  for row in lst:
    for i in range(len(row) - n+1):
      if sum(row[i:i+n]) == 0:
        spots += 1
  return spots

