
def half_a_fraction(fract):
  num, div = fract.split('/')
  num, div = int(num), int(div)
  if num % 2 == 0:
    num = num//2
  else:
    div = div*2
  return "{}/{}".format(num, div)

