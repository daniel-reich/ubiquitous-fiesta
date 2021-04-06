
def half_a_fraction(fract):
  num = list(map(int,fract.split("/")))
  if num[0]%2 == 0:
    num[0] = int(num[0]/2)
  else:
    num[1] = num[1]*2
  return str(num[0]) + "/" +str(num[1])

