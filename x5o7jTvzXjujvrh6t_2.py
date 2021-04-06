
def i_sqrt(n):
  c = 0
  while n >= 2:
    n **= 0.5
    c += 1
  return 'invalid' if n < 0 else c

