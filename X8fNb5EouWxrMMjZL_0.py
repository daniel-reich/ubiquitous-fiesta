
def collatz(num):
  new = [num // 2, num * 3 + 1][num % 2]
  return 0 if num == 1 else collatz(new) + 1

