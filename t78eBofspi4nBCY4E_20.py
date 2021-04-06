
def base_conv(n, b):
  digs = [chr(97+i) for i in range(26)]
  if type(n) is int:
    r = ''
    while n:
      r = digs[n%b] + r
      n //= b
    return r
  else:
    r = 0
    if any(d not in digs[:b] for d in n):
      return '{} is not a base {} number.'.format(n, b)
    for pos, i in enumerate(n[::-1]):
      r += digs.index(i)*b**pos
    return r

