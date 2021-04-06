
def half_a_fraction(fract):
  i1 = int(fract[fract.find("/")+1:])
  i2 = int(fract[:fract.find("/")])
  if i2%2 == 0:
   return "{}/{}".format(int(i2/2),int(i1))
  if i2%2 != 0:
   return "{}/{}".format(int(i2),int(i1*2))

