
def bit_rotate(n, m, d):
  b = bin(n)[2:]
  if not d:
    b = b[::-1]
  for i in range(m):
    f = b[-1]
    tmp = b[:-1]
    b = f+tmp
  if not d:
    b = b[::-1]
  return int(b, 2)

