
def switch_gravity_on(lst):
  n = len(lst)
  m = len(lst[0])
  piles = [[lst[i][j] for i in range(n)].count("#") for j in range(m)]
  return [[("#" if i+piles[j]>=n else "-") for j in range(m)] for i in range(n)]

