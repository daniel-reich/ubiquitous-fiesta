
def boom_intensity(n):
  if n<2:
    return 'boom'
  k = 'B'+'o'*n+'m'
  if n%5 == 0:
    k = k.upper()
  if n%2 == 0:
    k += '!'
  return k

