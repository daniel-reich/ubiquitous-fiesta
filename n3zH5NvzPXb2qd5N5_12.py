
def how_mega_is_it(n):
  if abs(n)<100:
    return 'not a mega milestone'
  i = 2
  while 10**i <= abs(n):
    if abs(n) < 10**(i+1): break
    else: i += 1
  return (i-2)*'MEGA ' + 'MEGA milestone'

