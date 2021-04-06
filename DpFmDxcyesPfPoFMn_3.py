
def isbn13(txt):
  digits = [int(digit) if digit != 'X' else 10 for digit in txt]
  if len(digits) == 10:
    s = sum([digits[i] * (10-i) for i in range(10)])
    if s % 11 == 0:
      digits = [9,7,8] + digits
      s = sum([digits[i] * (3 if i % 2 else 1) for i in range(12)])
      digits[-1] = 10 - (s % 10)
      return "".join(str(digit) for digit in digits)
  elif len(digits) == 13:
    s = sum([digits[i] * (3 if i % 2 else 1) for i in range(13)])
    if s % 10 == 0:
      return 'Valid'
  return 'Invalid'

