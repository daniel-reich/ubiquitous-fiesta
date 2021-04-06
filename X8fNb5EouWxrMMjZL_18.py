
def collatz(num):
  n = 0
  while num != 1:
    num = num // 2 if num % 2 == 0 else num * 3 + 1
    n += 1
  return n

