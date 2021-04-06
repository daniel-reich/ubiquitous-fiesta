
def is_valid_PIN(pin):
  if len(pin)== 4 or len(pin)==6:
    return pin.isdigit()
    
  else:
    return False

