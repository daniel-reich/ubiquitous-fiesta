
def bit_rotate(n, m, d):
  a = str(bin(n))[2:]
  b = (m % len(a)) * (-1 if d else 1)
  return int("0b" + a[b:] + a[0:b], 2)

