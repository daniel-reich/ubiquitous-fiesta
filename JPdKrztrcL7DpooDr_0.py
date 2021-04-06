
def collatz(n):
  if n == 1:
    return [0, 1]
  res = []
  while n != 1:
    res.append(n)
    n = n*3 + 1 if n%2 else n//2
  return [len(res), max(res)]

