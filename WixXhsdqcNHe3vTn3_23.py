
def how_bad(n):
  u = bin(n)[2:].count('1')
  a = []
  if u % 2 == 0:
    a = ['Evil']
  else:
    a = ['Odious']
  p = True
  for i in range(2, u):
    if u % i == 0:
      p = False
      break
  if p and (u != 1):
    a.append('Pernicious')
  return a

