
def bit_rotate(n, m, d):
  n = bin(n)
  m = m % (len(n) - 2)
  base = n[2:-m] if d else n[2+m:]
  suffix = n[-m:] if d else n[2:2+m]
  return int(suffix+base if d else base+suffix, 2)

