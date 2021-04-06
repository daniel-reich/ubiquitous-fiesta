
def i_sqrt(n, i = 0):
  if n < 0: return 'invalid'
  return i if n < 2 else i_sqrt(n**0.5, i+1)

