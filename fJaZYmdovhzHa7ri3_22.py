
def max_collatz(num):
  m = num
  while num > 1:
    num = [num // 2, num * 3 + 1][num % 2]
    m = max(num, m)
  return m

