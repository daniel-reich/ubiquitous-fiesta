
def sort_by_character(lst, n):
  d = {}
  for i in range(0,len(lst)):
    d[lst[i][n-1]] = i
  arr = []
  for k in sorted(d):
    arr.append(lst[d[k]])
  return arr

