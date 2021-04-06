
def collatz(n):
  if n == 1: return [0,1]
  ans = []
  while n != 1:
      if n % 2 == 0:
          n /=2
      else:
          n = (n * 3) + 1
      ans.append(int(n))
  return [len(ans), max(ans)]

