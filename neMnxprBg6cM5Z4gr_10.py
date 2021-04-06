
def arithmetic_progression(start, diff, n):
  res = [str(start)]
  while len(res) < n:
    res.append(str(int(res[len(res) - 1]) + diff))
  return ", ".join(res)

