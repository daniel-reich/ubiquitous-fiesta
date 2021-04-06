
def how_mega_is_it(n):
  mag = 0
  num = abs(n)
  while num >= 100:
    num //= 10
    mag += 1
  if abs(n) < 100: return 'not a mega milestone'
  else: return 'MEGA ' * mag + 'milestone'

