
def how_mega_is_it(n):
  return 'not a mega milestone' if abs(n) < 100 else len(str(abs(int(n))//100)) * 'MEGA ' + 'milestone'

