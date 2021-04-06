
def is_valid_PIN(pin):
  if len(pin)!=4 and len(pin)!=6: return False
  return pin.isdigit()

