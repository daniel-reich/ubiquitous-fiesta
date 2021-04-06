
def half_a_fraction(fract):
  s = fract.split("/")
  integer1 = int(s[0])
  integer2 = int(s[1])
  if integer1 % 2 == 1:
    integer2 = integer2 * 2
  else:
    integer1 = int(integer1 / 2)
  return str(integer1) + "/" + str(integer2)

