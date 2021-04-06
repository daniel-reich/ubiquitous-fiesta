
def is_valid_PIN(pin):
  if len(pin) == 4 or len(pin) == 6:
    if pin.isdecimal():
      return True
    else:
      return False
  else:
    return False

