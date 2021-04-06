
def pi(n):
  i = 1
  p = x = 3 * 10 ** (n + 10)
  while x: 
    x = x * i // ((i + 1) * 4)
    i += 2
    p += x // i
  return '3.' + str(p // 10 ** 10)[1:]

