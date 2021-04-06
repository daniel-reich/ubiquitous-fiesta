
def final(r, c, increments):
  arr = [[0 for _ in range(c)] for _ in range(r)]
  for n, t in increments:
    if t == 'r':
      for i in range(c): arr[int(n)][i] += 1
    else:
      for i in range(r): arr[i][int(n)] += 1
  return arr

