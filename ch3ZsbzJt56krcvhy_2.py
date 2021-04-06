
def square_root(n):                 # Big squares
  """ Return the square root of huge number """
  if n < (1<<50): return int(n**0.5)
  r = 1 << ((n.bit_length() + 1) >> 1)
  while True:
    num = (r+n//r) >> 1
    if num >= r:
      return r
    r = num

