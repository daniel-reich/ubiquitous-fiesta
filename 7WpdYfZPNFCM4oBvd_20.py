
def is_magic(m):
  ma = max(max(r) for r in m) if len(m) else 0
  rc = [sum(row) for row in m] + [sum(col) for col in zip(*m)]
  ds = [sum(m[i][i] for i in range(len(m)))] + [sum(m[i][-1-i] for i in range(len(m)))]
​
  return len(set(rc) | set(ds)) == 1 and ma <= len(m) ** 2

