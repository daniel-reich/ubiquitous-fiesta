
def half_a_fraction(fract):
  x,y=[int(i) for i in fract.split('/')]
  return str(x//2)+'/'+str(y) if x%2==0 else str(x)+'/'+str(y*2)

