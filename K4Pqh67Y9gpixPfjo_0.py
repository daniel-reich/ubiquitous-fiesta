
def is_valid_PIN(pin):
  return len(pin) in [4, 6] and pin.isdigit()

