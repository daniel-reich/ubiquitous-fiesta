
def _kaprekar(num):
  digits = '{:04}'.format(num)
  nSmall = int(''.join(sorted(digits)))
  nLarge = int(''.join(sorted(digits, reverse=True)))
  return nLarge - nSmall
​
def kaprekar(num):
  if num == 6174:
    return 0
  else:
    num = _kaprekar(num)
    return kaprekar(num) + 1

