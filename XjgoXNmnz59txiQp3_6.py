
def split(number):
  prod = 1
  while number > 4:
    prod *= 3
    number -= 3
  prod *= number
  return prod

