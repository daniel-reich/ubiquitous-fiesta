
def is_valid_PIN(pin):
  if pin.isdigit() and (len(pin)==4 or len(pin)==6):
    return True
  else:
    return False

