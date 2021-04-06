
def half_a_fraction(fract):
  fract = fract.split('/')
  if int(fract[0]) % 2 == 1:
     return(fract[0] + '/' + str(2 * int(fract[1])))
  else:
     return(str(int(fract[0])//2) + '/' + fract[1])

