
def turn_calc(num):
  return str(num)[::-1].translate(str.maketrans('01345678', 'OIEHSGLB', '.'))

