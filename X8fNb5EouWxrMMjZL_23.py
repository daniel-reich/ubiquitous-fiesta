
def collatz(num):
  x = 0
  while num != 1:
    if num % 2 == 0:
      num = num / 2
      x = x + 1
    elif num % 2 != 0:
      num = num * 3 + 1
      x = x + 1
  return x

