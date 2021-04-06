
def boom_intensity(n):
  if n < 2:
    return 'boom'
  if n%2==0 and n%5==0:
    return 'B'+'O'*n+'M!'
  if n%2==0:
    return 'B'+'o'*n+'m!'
  if n%5==0:
    return 'B'+'O'*n+'M'
  return 'B'+'o'*n+'m'

