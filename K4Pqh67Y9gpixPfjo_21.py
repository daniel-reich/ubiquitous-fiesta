
def is_valid_PIN(pin):
  a = len(pin)
  if (pin.isnumeric()) and (a == 4 or a == 6):
    return True 
  else:
    return False

