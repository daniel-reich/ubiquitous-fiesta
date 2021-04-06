
def ulam(q):
  ulm = [1, 2]
  n = 3
  while len(ulm) < q:
      c = 0
      for i in ulm:
        p = n - i
        if p < i and p in ulm:
          c += 1
        if c > 1:
          break
      if c== 1:
        ulm.append(n)
      n += 1
  return ulm[-1]

