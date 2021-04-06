
def half_a_fraction(fract):
  fraction = fract.split("/")
  if int(fraction[0]) % 2 == 0:
    return '{}/{}'.format(int(int(fraction[0])/2), int(fraction[1]))
  return '{}/{}'.format(int(fraction[0]), int(fraction[1])*2)

