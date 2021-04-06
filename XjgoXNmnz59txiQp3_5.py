
def split(number):
  power = number//3
  leftover = number % 3
  if number == 1:
    return 1
  elif leftover == 1:
    return 3**(power-1)*2**2
  elif leftover == 0:
    return 3**power
  elif number == 1:
    return 1
  else:
    return 3**power*leftover

