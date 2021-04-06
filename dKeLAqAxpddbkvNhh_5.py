
def group_seats(lst, n):
  ctr = 0
  for i in range(len(lst)):
    for j in range(len(lst[i])-n+1):
      if sum(lst[i][j:j+n]) == 0:
        ctr += 1
  return ctr

