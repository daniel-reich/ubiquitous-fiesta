
def collatz(n):
  N = [n]
  while n - 1:
    N += [[n // 2, n * 3 + 1][n % 2]]
    n = N[-1]
  return len(N), max(N)

