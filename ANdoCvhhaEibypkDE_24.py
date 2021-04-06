
def closing_in_sum(n):
  x, n = 0, str(n)
  while len(n)>1:
    x += int(n[0]+n[-1])
    n = n[1:-1]
  return x + int(n) if n else x

