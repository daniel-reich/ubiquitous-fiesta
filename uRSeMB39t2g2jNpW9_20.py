
def turn_calc(num):
  chars = 'OIZEHSGLB'
  return ''.join(chars[int(c)] for c in str(num)[::-1] if c in '012345678')

