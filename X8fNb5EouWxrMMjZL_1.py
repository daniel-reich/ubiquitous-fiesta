
def collatz(num):
  return 1 + collatz([num // 2, num * 3 + 1][num % 2]) if num > 1 else 0

