
def collatz(n):
  mx, ctr = n, 0
  while n != 1:
    n = n / 2 if n % 2 == 0 else n * 3 + 1
    if n > mx: mx = n
    ctr += 1
  return [ctr, mx]

