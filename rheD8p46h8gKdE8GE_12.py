
def grayscale(lst):
  m,n = len(lst), len(lst[0])
  for i in range(m):
    for j in range(n):
      lst[i][j] = [round(sum(max(0,min(e,255)) for e in lst[i][j])/3)]*3
  return lst

