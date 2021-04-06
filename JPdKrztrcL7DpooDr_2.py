
def collatz(n):
  a = []
  counter = 0
  if n == 1:
    return [0,1]
  while True:
    if n == 1:
      return [counter, max(a)]
    else:
      if n % 2 == 0:
        n = n // 2
        a.append(n)
        counter += 1
      else:
        n = n*3 + 1
        a.append(n)
        counter += 1

