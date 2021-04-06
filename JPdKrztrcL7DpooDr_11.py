
def collatz(n):
  print(n)
  count = 0
  high = 0
  if n == 1:
    count = 0
    high = 1
  while n != 1:
    count = count + 1
    if high < n:
      high = n
    if n % 2 == 0:
      n = n / 2
    else:
      n = (n * 3) + 1
  print(count, high)
  return([count, high])

