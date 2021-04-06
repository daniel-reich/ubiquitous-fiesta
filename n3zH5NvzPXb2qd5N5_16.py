
def how_mega_is_it(n):
  if n < 100 and n >= 0: return 'not a mega milestone'
  l = len(str(int(abs(n)))) - 2
  s = 'MEGA ' * l
  return s + 'milestone'

