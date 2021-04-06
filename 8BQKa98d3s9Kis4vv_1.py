
def final(r, c, inc):
  res = [[0 for i in range(c)] for j in range(r)]
​
  for n, l in inc:
    if l == 'r':
      for j in range(c):
        res[int(n)][j] += 1
    else:
      for j in range(r):
        res[j][int(n)] += 1
  return res

