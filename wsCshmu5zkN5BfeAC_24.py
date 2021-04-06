
def divisible_by_left(n):
  return [False] + [int(j) % int(i) == 0 if int(i) != 0 else False for i, j in zip(str(n), str(n)[1:])]

