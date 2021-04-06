
def split(number):
  if (number < 5):
    return  number
  rem = number % 3
  div3 = number//3
  if (rem == 2):
    return 3 ** (div3) * 2
  return 3 ** (div3-1) * (3 + rem)

