
def divisible_by_left(n):
  n = str(n)
  return [False] + [a != "0" and int(b) % int(a) == 0 for a, b in zip(n, n[1:])]

