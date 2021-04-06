
def happy(n):
  digits = [x for x in str(n)]
  for _ in range(9):
    total = 0
    for x in digits:
      total = total + (int(x) * int(x))
    if int(total) == 1:
      return True
    digits = [x for x in str(total)]
  return False

