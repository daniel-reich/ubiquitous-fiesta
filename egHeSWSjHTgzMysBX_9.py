
def half_a_fraction(fract):
  fract_list = fract.split('/')
  if int(fract_list[0])%2==0:
    fract_list[0] = str(int(fract_list[0])//2)
  else:
    fract_list[1] = str(int(fract_list[1])*2)
  return '/'.join(fract_list)

