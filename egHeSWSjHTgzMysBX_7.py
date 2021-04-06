
def half_a_fraction(fract):
  fr = list(map(int,fract.split("/")))
  if int(fr[0]) % 2 == 0:
    return str(fr[0]//2)+"/"+str(fr[1])
  else:
    return str(fr[0])+"/"+str(fr[1]*2)

