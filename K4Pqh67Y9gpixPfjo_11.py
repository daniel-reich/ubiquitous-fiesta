
def is_valid_PIN(pin):
  if len(pin) in [4, 6]:
    return pin.isdigit()
  else:
    return False

