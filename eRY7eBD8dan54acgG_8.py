
def is_checkerboard(lst):
  n = len(lst)
  v1 = [i % 2 == 0 for i in range(n)]
  v0 = [i % 2 == 1 for i in range(n)]
  v, k = [v0, v1], 0
  if lst[0][0] == 1:
    k = 1
  for i in range(len(lst)):
    if lst[i] != v[k]:
      return False
    k = 1 - k
  return True

