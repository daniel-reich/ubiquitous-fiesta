
def divisible_by_left(n):
  n = str(n)
  return [False] + [int(b) % (10 if int(a) == 0 else int(a)) == 0 for a, b in zip(n[:-1], n[1:])]

