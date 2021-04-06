
def ones_infection(arr):
  l = arr
  l2 = [(r,c)for r in range(len(l)) for c in range(len(l[r])) if l[r][c] == 1]
  rows = [i[0] for i in l2]
  cols = [i[1] for i in l2]
  for row in range(len(l)):
    if row in rows:
      l[row] = [1 for i in range(len(l[row]))]
    for col in cols:
        l[row][col] = 1
  return(l)

