
def josephus(n, i):
  if n == 1:
    return 1
  else:
    return (josephus(n - 1, i) + i - 1) % n + 1

