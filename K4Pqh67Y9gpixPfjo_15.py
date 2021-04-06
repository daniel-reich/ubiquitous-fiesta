
def is_valid_PIN(pin):
  if pin.isnumeric() and len(pin) == 4 or len(pin) == 6:
    return True
  else:
    return False

