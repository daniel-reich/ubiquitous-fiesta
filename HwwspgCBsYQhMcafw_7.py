
def super_digit(n, k):
  if int(n) <= 9:
    return int(n)
  return super_digit(str(sum(list(map(int,list(str(n)))))*k), 1)

