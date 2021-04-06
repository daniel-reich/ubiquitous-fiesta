
def closing_in_sum(n):
  n, res = str(n) ,0
  while len(n) > 1:
    res += int(n[0]+n[-1])
    n = n[1:-1]
  return res + int(n) if n else res

