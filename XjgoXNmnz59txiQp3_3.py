
def split(number):
  import math
  if number > 2:
    threes = math.floor((number - 2) / 3)
    remainder = number % 3 + 3
    if remainder == 5:
      remainder = 2
    product = 3 ** threes * remainder
  else:
    product = number
  return product

