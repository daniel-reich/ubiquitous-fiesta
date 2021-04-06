
def how_mega_is_it(m):
  k = len(str(abs(int(m))))-2
  return ['not a mega milestone', 'MEGA '*k+'milestone'][k > 0]

