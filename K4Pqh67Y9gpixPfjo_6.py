
def is_valid_PIN(pin):
  return pin.isdigit() and len(pin) in (4, 6)

