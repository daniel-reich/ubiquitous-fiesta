
def bit_rotate(n, m, d):
  s = bin(n).lstrip('0b')
  m %= len(s)
  if d:
    r = s[-m:] + s[:-m]
  else:
    r = s[m:] + s[:m]
  return int('0b'+r, base=2)

