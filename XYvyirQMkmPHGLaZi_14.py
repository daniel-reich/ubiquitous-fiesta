
def boom_intensity(n):
  if n<2: return 'boom'
  a='B'+'o'*n+'m'+'!'*(n%2==0)
  return n%5 and a or a.upper()

