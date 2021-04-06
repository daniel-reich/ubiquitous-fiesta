
def complete_square(mtx):
  n, m = len(mtx), len(mtx[0])
  if n > m:
    for row in mtx:
      for i in range(n-m):
        row.append(0)
  else:
    for i in range(m-n):
      mtx.append([0 for i in range(m)])
  return mtx

