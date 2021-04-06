
def how_mega_is_it(n):
  return ('MEGA ' * (len(str(abs(int(n)))) - 2) or 'not a mega ') + 'milestone'

