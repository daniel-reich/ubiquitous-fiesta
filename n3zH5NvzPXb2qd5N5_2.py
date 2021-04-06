
def how_mega_is_it(n):
  if abs(n) < 100: return "not a mega milestone"
  
  return (len(str(abs(int(n)))) - 2) * 'MEGA ' + 'milestone'

