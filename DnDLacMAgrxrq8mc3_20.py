
def blah_blah(txt, n):
  u = txt.split(' ')[::-1]
  for i in range(min(n, len(u))):
    u[i] = 'blah'
  return ' '.join(u[::-1]) + '...'

