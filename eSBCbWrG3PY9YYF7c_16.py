
def sexagenary(year):
  els = ['wood', 'wood', 'fire', 'fire', 'earth', 'earth', 'metal','metal', 'water', 'water']
  yrs = ['rat', 'ox', 'tiger', 'rabbit', 'dragon', 'snake', 'horse', 'sheep', 'monkey', 'rooster', 'dog', 'pig']
  dif = year - 1924
  i1 = dif%12
  i2 = dif%10
  s = els[i2].title() + ' ' + yrs[i1].title()
  return s

