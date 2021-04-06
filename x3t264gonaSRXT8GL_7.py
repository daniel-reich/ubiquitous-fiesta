
def repeating_cycle(n):
  if n % 2 == 0 or n % 5 == 0:
    return -1
  r = 10 % n
  c = 1
  while r != 1:
    r = r * 10 % n
    c += 1
  return c

