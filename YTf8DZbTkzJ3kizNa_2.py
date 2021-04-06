
def moran(n):
  hash = n / sum(map(int, str(n)))
  if hash % 1 == 0:
    if all(hash % i != 0 for i in range(2, int(hash))):
      return 'M'
    else:
      return 'H'
  return 'Neither'

