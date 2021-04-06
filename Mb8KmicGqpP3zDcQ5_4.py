
def josephus(n, i):
  v = [1] * n
  k = 1
  while True:
    for x in range(n):
      if sum(v) == 1:
        return v.index(1) + 1
      elif v[x] == 1:
        if k == i:
          v[x] = 0
          k = 1
        else:
          k += 1

